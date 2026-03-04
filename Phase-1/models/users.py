from Databases import Base
from sqlalchemy import Column, Integer, String



# Example of an ORM model (table definition)
class User(Base):
    __tablename__ = 'users'  # name of the table in the database

    id = Column(Integer, primary_key=True, index=True) ## index=True: creates an index on this column for faster queries
    name = Column(String, index=True) ## index=True: creates an index on this column for faster queries
    email = Column(String, unique=True, index=True) ## index=True: creates an index on this column for faster queries
    


        # created_at = Column(DateTime)

        # updated_at = Column(DateTime)

        # is_active = Column(Boolean)
    ## production ready tables should have created_at, updated_at, is_active columns 
    # to track record creation, updates, and soft deletion (is_active=False instead of deleting records).

'''
Note : we dont use index for every table column, 
we use it for columns that are frequently searched or used in WHERE clauses to speed up query performance. 
However, using too many indexes can slow down write operations (INSERT, UPDATE, DELETE) because the database has to maintain the indexes.
Therefore, it's important to choose which columns to index based on your application's query patterns.

If U dont sql: go and sql first as foudnatation of it then come back to this file and read it again, you will understand it better beacause whole orm is based on sql and how it works.
'''
