
## it is main file where we will create the tables in the database based on the ORM models.

from Databases import Base, engine
import models ## import the models to ensure they are registered with SQLAlchemy before creating tables

Base.metadata.create_all(engine)   ## creates the tables in the database based on the ORM models defined (like User) if they don't already exist.

print("Tables created successfully")