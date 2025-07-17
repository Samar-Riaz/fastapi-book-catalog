from sqlalchemy.orm import Session
from app.models.book import Book
from app.schemas.book import BookCreate, BookUpdate

def get_books(db: Session):
    """
    Retrieve all books from the database.

    Args:
        db (Session): SQLAlchemy database session.

    Returns:
        List[Book]: A list of all book records.
    """
    return db.query(Book).all()


def get_book(db: Session, book_id: int):
    """
    Retrieve a single book by its ID.

    Args:
        db (Session): SQLAlchemy database session.
        book_id (int): ID of the book to retrieve.

    Returns:
        Book | None: The Book object if found, otherwise None.
    """
    return db.query(Book).filter(Book.id == book_id).first()


def create_book(db: Session, book: BookCreate):
    """
    Create a new book record in the database.

    Args:
        db (Session): SQLAlchemy database session.
        book (BookCreate): Book creation data from request body.

    Returns:
        Book: The newly created book.
    """
    # Convert Pydantic model to dictionary and unpack into Book model
    db_book = Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)  # Reload instance from DB after commit
    return db_book


def update_book(db: Session, book_id: int, book: BookUpdate):
    """
    Update an existing book record.

    Args:
        db (Session): SQLAlchemy database session.
        book_id (int): ID of the book to update.
        book (BookUpdate): Updated book fields.

    Returns:
        Book | None: The updated book if found, otherwise None.
    """
    db_book = get_book(db, book_id)
    if db_book:
        # Dynamically update fields
        for key, value in book.model_dump().items():
            setattr(db_book, key, value)
        db.commit()
        db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: int):
    """
    Delete a book from the database.

    Args:
        db (Session): SQLAlchemy database session.
        book_id (int): ID of the book to delete.

    Returns:
        Book | None: The deleted book if found, otherwise None.
    """
    db_book = get_book(db, book_id)
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book
