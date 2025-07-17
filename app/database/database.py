from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite database URL — for a local file-based DB called 'books.db'
SQLALCHEMY_DATABASE_URL = "sqlite:///./books.db"

# Create a SQLAlchemy engine instance.
# 'check_same_thread=False' is specific to SQLite and allows usage of the connection across multiple threads.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False}  # Needed for SQLite in multithreaded FastAPI apps
)

# Create a configured "SessionLocal" class.
# Each instance of SessionLocal will be a new database session.
SessionLocal = sessionmaker(
    autocommit=False,  # Commit must be called explicitly
    autoflush=False,   # Prevents automatic flush before queries
    bind=engine        # Bind session to the engine (database)
)

# Base class for all ORM models to inherit from.
# This will be used by SQLAlchemy to define tables and classes.
Base = declarative_base()
