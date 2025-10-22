from platform import release
from typing import Optional
from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()


class Movie:
    id: int
    title: str
    director: str
    genre: str
    rating: int
    released_year: int

    def __init__(self, id, title, director, genre, rating, released_year):
        self.id = id
        self.title = title
        self.director = director
        self.genre = genre
        self.rating = rating
        self.released_year = released_year


class MovieRequest(BaseModel):
    id: Optional[int] = Field(description="ID is not needed on create", default=None)
    title: str = Field(min_length=3)
    director: str = Field(min_length=15)
    genre: str = Field(min_length=1, max_length=10)
    rating: float = Field(gt=-1, lt=6)
    released_year: int = Field(gt=1980, lt=2025)

    model_config = {
    "json_schema_extra":{
        "example": {
            "title": "A new movie",
            "director": "A movie director",
            "genre" : "Comedy",
            "rating": 5,
            "released_date": 2020,
        }
    }
 }


MOVIES = [
    Movie(1, 'Inception', 'Christopher Nolan', 'Sci-Fi', 4.8, 2010),
    Movie(2, 'The Godfather', 'Francis Ford Coppola', 'Crime', 4.7, 1972),
    Movie(3, 'Spirited Away', 'Hayao Miyazaki', 'Animation', 4.8, 2001),
    Movie(4, 'Parasite', 'Bong Joon-ho', 'Thriller', 4.8, 2019),
    Movie(5, 'Pulp Fiction', 'Quentin Tarantino', 'Drama', 4.5, 1994),
]

@app.get("/movies", status_code=status.HTTP_200_OK)
def read_all_movies():
    return MOVIES


@app.get("/movies/{movie_id}", status_code=status.HTTP_200_OK)
def read_movie(movie_id: int = Path(gt=0)):
    for movie in MOVIES:
        if movie.id == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")


@app.get("/movies/", status_code=status.HTTP_200_OK)
def read_movie_by_rating(movie_rating: float = Query(gt=0, lt=6)):
    movies_to_return = []
    for movie in MOVIES:
        if movie.rating == movie_rating:
            movies_to_return.append(movie)
    return movies_to_return


@app.get("/movies/released_year/", status_code=status.HTTP_200_OK)
def read_movie_by_released_year(released_date: int = Query(gt=1980, lt=2025)):
    movie_to_return = []
    for movie in MOVIES:
        if movie.released_year == released_date:
            movie_to_return.append(movie)
    return movie_to_return


@app.post("/create-movie", status_code=status.HTTP_201_CREATED)
def create_movie(movie_request: MovieRequest):
    new_movie = Movie(**movie_request.model_dump())
    MOVIES.append(find_movie_id(new_movie))


def find_movie_id(movie: Movie):
    movie.id = 1 if len(MOVIES) == 0 else MOVIES[-1].id + 1
    return movie


@app.put("/movies/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
def update_movies(movies: MovieRequest):
    movie_changed = False
    for i in range(len(MOVIES)):
        if MOVIES[i].id == movies.id:
            MOVIES[i]= movies
            movie_changed = True
    if not movie_changed:
        raise HTTPException(status_code = 404, detail="Movie not found")


@app.delete("/movies/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_movies(movie_id: int):
    movie_deleted = False
    for i in range(len(MOVIES)):
        if MOVIES[i].id == movie_id:
            MOVIES.pop(i)
            movie_deleted = True
            break
    if not movie_deleted:
        raise HTTPException(status_code=404, detail="Movie not found")