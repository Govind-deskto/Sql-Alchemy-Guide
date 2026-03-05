from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./Database/sqlite3.db"  # we will use sqlite for simplicity, but you can use other databases like PostgreSQL or MySQL by changing the URL accordingly.

engine = create_engine(
    DATABASE_URL,
    pool_size=20,
    max_overflow=10
)

'''
1. --- pool_size ----------
 Number of permanent database connections kept ready in the pool.
    These connections are reused for incoming requests to avoid creating
    a new database connection every time (which is slow).
    # 2. --- max_overflow ----------
    Extra temporary connections allowed when the pool_size limit is reached.
        Example: if pool_size=20 and all are in use, SQLAlchemy can create
        up to 10 additional connections (total = 30). These overflow
        connections are temporary and closed after use.         
'''


SessionLocal = sessionmaker(
    autocommit=False,
    # changes are NOT saved automatically, you must call db.commit()

    autoflush=False,
    # SQLAlchemy will not automatically send pending changes to DB

    bind=engine
    # connects this session manager to the engine
)

'''
in Orm Tables = classes: we  Define Because access of each table And Inherit it with our global platform As a Base.
'''

Base = declarative_base()
# base class for all ORM models (tables will inherit from this: imagine  the platform where whole your tables are defined on this Base( on creation ),Therefore we will inherit from this Base class when defining our ORM models (tables) in other files.
## now  go to models folder to understand hiw the tables are defined and how they inherit from this Base class.

