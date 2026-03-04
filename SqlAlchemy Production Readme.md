# 🐍 SQLAlchemy Production Guide (Backend Engineer Level)

A practical guide to using **SQLAlchemy in real production backends**
(mid‑size startup level).\
Focus: clean architecture, performance, and maintainable database
layers.

------------------------------------------------------------------------

# 📦 Tech Stack Example

Typical production backend stack:

    FastAPI
    SQLAlchemy
    PostgreSQL
    Alembic
    Redis
    Docker

------------------------------------------------------------------------

# 📁 Recommended Project Structure

    backend/
    │
    ├── app/
    │   ├── db/
    │   │   ├── database.py
    │   │   ├── models.py
    │   │
    │   ├── crud/
    │   │   ├── user_crud.py
    │   │
    │   ├── schemas/
    │   │
    │   ├── api/
    │   │
    │   └── services/
    │
    ├── alembic/
    └── main.py

  Folder     Purpose
  ---------- -----------------------------------
  db         database configuration and models
  crud       database operations
  schemas    request/response validation
  api        HTTP endpoints
  services   business logic

------------------------------------------------------------------------

# ⚙️ Database Configuration

`database.py`

``` python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://user:password@localhost/db"

engine = create_engine(
    DATABASE_URL,
    pool_size=20,
    max_overflow=10
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
```

### Important Parameters

  Parameter      Meaning
  -------------- ---------------------------------
  pool_size      number of active DB connections
  max_overflow   extra temporary connections

------------------------------------------------------------------------

# 🔄 Session Per Request Pattern

Always create **one session per request**.

``` python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

Why this matters:

-   prevents connection leaks
-   keeps transactions isolated
-   safe for concurrent users

------------------------------------------------------------------------

# 🧱 Creating Models

Example model:

``` python
from sqlalchemy import Column, Integer, String
from .database import Base

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
```

### Production Best Practices

  Rule             Reason
  ---------------- ------------------
  index=True       faster queries
  unique=True      avoid duplicates
  nullable=False   data integrity

------------------------------------------------------------------------

# 🧠 CRUD Layer

Keep DB logic separate from API routes.

`crud/user_crud.py`

``` python
from sqlalchemy.orm import Session
from app.db.models import User

def create_user(db: Session, name: str, email: str):
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()
```

------------------------------------------------------------------------

# 🔗 Relationships

Example: **User → Posts (One to Many)**

    User
      └── Posts

User model:

``` python
posts = relationship("Post", back_populates="user")
```

Post model:

``` python
user_id = Column(Integer, ForeignKey("users.id"))
user = relationship("User", back_populates="posts")
```

------------------------------------------------------------------------

# ⚡ Avoid N+1 Query Problem

Bad example:

``` python
users = session.query(User).all()

for user in users:
    print(user.posts)
```

Solution:

``` python
from sqlalchemy.orm import joinedload

users = session.query(User).options(
    joinedload(User.posts)
)
```

------------------------------------------------------------------------

# 📄 Pagination

Never load full tables.

Correct pattern:

``` python
query.offset(skip).limit(limit)
```

Example:

``` python
users = db.query(User).offset(20).limit(10).all()
```

------------------------------------------------------------------------

# 🔎 Filtering

``` python
db.query(User).filter(User.email == "user@mail.com")
```

Multiple conditions:

``` python
db.query(User).filter(
    User.name == "Krishna",
    User.id > 5
)
```

------------------------------------------------------------------------

# 🔗 Joins

Example join query:

``` python
db.query(User).join(Post).filter(Post.title == "Hello")
```

SQL Equivalent:

``` sql
SELECT *
FROM users
JOIN posts ON users.id = posts.user_id;
```

------------------------------------------------------------------------

# 📊 Aggregations

Count example:

``` python
from sqlalchemy import func

db.query(func.count(User.id)).scalar()
```

Group by example:

``` python
db.query(Post.user_id, func.count(Post.id)).group_by(Post.user_id)
```

------------------------------------------------------------------------

# 🚀 Bulk Inserts

Fast insert for large data sets.

``` python
session.bulk_save_objects([
    User(name="A"),
    User(name="B"),
])
```

------------------------------------------------------------------------

# 🔁 Database Migrations (Alembic)

Install:

    pip install alembic

Initialize:

    alembic init alembic

Create migration:

    alembic revision --autogenerate -m "create users table"

Apply migration:

    alembic upgrade head

------------------------------------------------------------------------

# ⚡ Performance Best Practices

### Always index frequently queried columns

    email
    username
    foreign keys

### Avoid SELECT \*

Bad:

``` sql
SELECT *
```

Better:

``` python
select(User.id, User.name)
```

### Use Pagination

Never load entire tables.

### Use eager loading

    joinedload
    selectinload

------------------------------------------------------------------------

# 🧪 Debugging Queries

Enable SQL logs:

``` python
engine = create_engine(DATABASE_URL, echo=True)
```

This prints generated SQL queries.

------------------------------------------------------------------------

# 🧠 Production Tips

Good backend engineers:

-   design efficient queries
-   understand indexes
-   prevent N+1 queries
-   use migrations properly
-   structure database layers cleanly

ORM knowledge alone is **not enough**.

------------------------------------------------------------------------

# 📚 What to Master Next

To reach **senior backend level**, learn:

-   database indexing strategy
-   query optimization
-   transactions & isolation levels
-   async SQLAlchemy
-   caching with Redis
-   database monitoring

------------------------------------------------------------------------

# ⭐ Final Note

If you can confidently implement everything in this README,\
you are **ready to work on SQLAlchemy production backends in most
startups**.
