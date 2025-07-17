from sqlalchemy import Column, Integer, String
from app.database.database import Base

class Book(Base):
    """
    SQLAlchemy ORM model representing a 'Book' record in the database.
    Inherits from the Base class defined in app.database.database.
    """

    __tablename__ = "books"  # Name of the table in the database

    id = Column(Integer, primary_key=True, index=True)
    """
    Unique identifier for each book.
    - Primary key
    - Indexed for fast lookup
    """

    title = Column(String, index=True)
    """
    Title of the book.
    - Indexed to improve query performance on title searches
    """

    author = Column(String, index=True)
    """
    Author of the book.
    - Indexed to improve filtering/searching by author
    """

    published_year = Column(Integer)
    """
    The year the book was published.
    - Integer type
    """

    summary = Column(String, nullable=True)
    """
    Optional summary or description of the book.
    - Nullable string field
    """
