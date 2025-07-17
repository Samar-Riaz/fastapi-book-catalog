from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class BookBase(BaseModel):
    """
    Base schema for book data used in both input and output operations.

    Attributes:
        title (str): Title of the book.
        author (str): Author of the book.
        published_year (int): Year the book was published (between 0 and 2100).
        summary (Optional[str]): Optional summary or description of the book.
    """
    title: str
    author: str
    published_year: int = Field(..., ge=0, le=2100, description="Year between 0 and 2100")
    summary: Optional[str] = None

class BookCreate(BookBase):
    """
    Schema for creating a new book.
    Inherits all fields from BookBase.
    """
    pass

class BookUpdate(BookBase):
    """
    Schema for updating an existing book.
    Inherits all fields from BookBase.
    """
    pass

class BookOut(BookBase):
    """
    Schema for returning book data in API responses.

    Attributes:
        id (int): Unique identifier for the book.
    """
    id: int

    model_config = ConfigDict(from_attributes=True)  # Enables ORM mode
