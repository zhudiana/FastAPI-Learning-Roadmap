# 🚀 FastAPI Learning Roadmap

📚 A complete roadmap to mastering FastAPI — from Python fundamentals to advanced backend development.  
Includes structured notes, curated resources, and example projects.

---

##  What’s Inside

- **01 – Python Fundamentals**  
  Build a solid foundation in functions, OOP, type hints, data structures, virtual environments, and CLI tools.

- **02 – FastAPI Setup & Basics**  
  Learn to install FastAPI, write endpoints using path and query parameters, define Pydantic models, and explore auto-generated docs (Swagger UI / ReDoc).

- **03 – Projects: Request Methods & Flow**  
  Practice building examples that handle GET, POST, PUT, DELETE and advanced request–response patterns.

- **04 – FastAPI in Motion**  
  Dive deeper into client/server flow, routers, middleware, and dependency injection.

- **05 – Structuring with SQLite (and transitioning to Production DBs)**  
  Use SQLite with SQLAlchemy, then upgrade to PostgreSQL/MySQL as your app scales.

- **06 – Authentication & Authorization**  
  Set up user models, password hashing, JWT authentication with role-based permissions, and protected endpoints.

- **07 – Authenticated Access Flow**  
  Learn how to log in via OAuth2, decode JWTs, and ensure users only access their own data.

- **08 – Managing Migrations with Alembic**  
  Generate migrations, apply them (upgrade/downgrade), and synchronize your FastAPI models.

- **09 – Adding DB Columns Safely**  
  Example migration: adding the `phone_number` field with null-handling and updating models.

- **10 – Testing in FastAPI**  
  Write tests using `pytest`, utilize fixtures vs. class-style setups, and create clean, maintainable tests.

---

##  How to Use This Roadmap

1. Start from **Python Fundamentals**, unless you're already confident in them.
2. Progress through each section in order, working through the **notes** and applying them hands-on.
3. Open the `/notes` folder for step-by-step explanations and real examples.
4. Practice using Swagger UI, look at migrations in Alembic, and test your ideas with `pytest`.

---

##  Resources

- [FastAPI Official Docs](https://fastapi.tiangolo.com)  
- [SQLAlchemy ORM Docs](https://docs.sqlalchemy.org)  
- [Pydantic Validation Guide](https://docs.pydantic.dev)  

---

##  Goal

By following this roadmap, you'll build scalable, secure APIs with FastAPI, backed by PostgreSQL, migrations, authentication, and solid testing practices.
