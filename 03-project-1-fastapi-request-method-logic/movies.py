from fastapi import Body, FastAPI

app = FastAPI()

MOVIES = [
    {"title": "Inception", "director": "Christopher Nolan", "genre": "Sci-Fi"},
    {"title": "Interstellar", "director": "Christopher Nolan", "genre": "Sci-Fi"},
    {"title": "The Godfather", "director": "Francis Ford Coppola", "genre": "Crime"},
    {"title": "Spirited Away", "director": "Hayao Miyazaki", "genre": "Animation"},
    {"title": "Parasite", "director": "Bong Joon-ho", "genre": "Thriller"},
    {"title": "Pulp Fiction", "director": "Quentin Tarantino", "genre": "Drama"},
]

# Get all movies
@app.get("/movies")
def read_all_movies():
    return MOVIES

# Get a movie by its title (search a movie with a title) (with dynamic path parameter)
@app.get("/movies/{title}")
def read_movie(title):
    for movie in MOVIES:
      if movie.get('title').casefold() == title.casefold():
        return movie

# Get a movie by its genre (search a movie with a genre) (with query parameter)
@app.get("/movies/")
def read_genre_by_query(genre: str):
    movies_to_return = []
    for movie in MOVIES:
        if movie.get('genre').casefold() == genre.casefold():
            movies_to_return.append(movie)
    return movies_to_return

# Get a movie by its director and genre(search a movie with a director and genre) (with dynamic path parameter and query parameter)
@app.get("/movies/by_director/{movie_director}")
def read_genre_by_query(movie_director: str, genre: str):
    movies_to_return = []
    for movie in MOVIES:
        if movie.get('director').casefold() == movie_director.casefold() and movie.get('genre').casefold() == genre.casefold():
            movies_to_return.append(movie)
    return movies_to_return

# Add a new movie 
@app.post("/movies/create_movie")
def create_movie(new_movie=Body()):
    MOVIES.append(new_movie)

# Update an existing movie by searching with title
@app.put("/movies/update_movie")
def update_movie(updated_movie=Body()):
    for i in range(len(MOVIES)):
        if MOVIES[i].get("title").casefold() == updated_movie.get("title").casefold():
            MOVIES[i] = updated_movie

# Delete an existing movie by searching with title
@app.delete("/movies/delete_movie/{title}")
def delete_movie(title: str):
    for i in range(len(MOVIES)):
        if MOVIES[i].get("title").casefold() == title.casefold():
            MOVIES.pop(i)
            break
