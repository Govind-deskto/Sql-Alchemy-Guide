
# SQLAlchemy ORM Learning Project (Phase‑1)

This repository documents my **hands‑on learning journey with SQLAlchemy ORM**.
The goal of this project is to **understand database interaction in Python step‑by‑step**, starting from basic setup and moving toward production‑level backend patterns.

This repository will grow in **phases**, where each phase introduces new backend engineering concepts.

---

# Phase‑1 Overview

Phase‑1 focuses on **core SQLAlchemy fundamentals** and building a simple but structured project layout.

In this phase I learned how to:

• Setup SQLAlchemy engine and database connection
• Create ORM models (tables as Python classes)
• Create tables automatically using metadata
• Perform CRUD operations
• Organize backend code into logical folders
• Use Git with proper `.gitignore` practices
• Document code with detailed comments

---

# Project Structure

```
ORM-SQLALECHMY/
│
├── Database/
│   └── user.db            # SQLite database file
│
├── env/                   # Python virtual environment (ignored in git)
│
├── models/                # ORM model definitions (tables)
│   ├── users.py
│   └── items.py
│
├── Cruds/                 # CRUD operation scripts
│
├── Setup/                 # Setup / notes / helper files
│
├── Databases.py           # Engine, session, Base configuration
├── main.py                # Application startup / table creation
├── .gitignore             # Ignore env, cache, db files
└── Readme.md
```

---

# Key Concepts Covered in Phase‑1

## 1. Database Engine

The SQLAlchemy **engine** manages the connection to the database.

Example:

```python
engine = create_engine(DATABASE_URL)
```

The engine is responsible for:

• Managing database connections
• Executing SQL queries
• Connection pooling

---

## 2. ORM Models

Tables are defined as **Python classes**.

Example:

```python
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
```

This maps:

Python Class → Database Table

---

## 3. Sessions

Sessions are used to interact with the database.

```
db = SessionLocal()
```

The session performs:

• Insert operations
• Query operations
• Updates
• Deletes

---

## 4. CRUD Operations

Basic database operations:

Create
```
db.add(user)
db.commit()
```

Read
```
db.query(User).all()
```

Update
```
user.name = "Updated Name"
db.commit()
```

Delete
```
db.delete(user)
db.commit()
```

---

# Why This Project Exists

This repository is designed as:

• A learning log
• A reference guide
• A step‑by‑step documentation of backend learning

Every file contains **detailed comments explaining the logic**, making it beginner friendly.

---

# Phase‑2 (Next)

In the next phase the project will expand to include:

• Proper CRUD modules
• Better project structure
• Relationships between tables
• Query optimization
• Modular backend design
• Possibly API integration (FastAPI / Flask)

Phase‑2 will continue in a **separate branch** and later be merged into `main`.

---

# Learning Approach

This repository follows a simple rule:

Write code → Understand it → Document it.

Every concept is explained through **code comments and README documentation**.

---

# Author

Learning & experimenting with Python backend development and SQLAlchemy ORM.
