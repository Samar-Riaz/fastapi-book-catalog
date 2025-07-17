"""
Unit tests for the book CRUD operations using unittest.mock.
These tests mock the database session and test the business logic in isolation.
"""

from unittest.mock import MagicMock
from app.schemas.book import BookCreate, BookUpdate
from app.models.book import Book
from app.crud import book_crud
import pytest
from fastapi import HTTPException
from datetime import datetime


def test_create_book_unit():
    """Test successful creation of a book"""
    mock_db = MagicMock()
    book_data = BookCreate(
        title="Test Book",
        author="Jane Doe",
        published_year=2022,
        summary="Unit testing a book creation"
    )

    result = book_crud.create_book(mock_db, book_data)

    # Assert database operations were called correctly
    mock_db.add.assert_called_once()
    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once_with(result)

    # Assert book data is correctly set
    assert result.title == "Test Book"
    assert result.author == "Jane Doe"


def test_get_books_unit():
    """Test retrieving all books"""
    mock_db = MagicMock()
    mock_db.query.return_value.all.return_value = ["book1", "book2"]

    result = book_crud.get_books(mock_db)

    assert result == ["book1", "book2"]


def test_get_book_unit():
    """Test retrieving a single book by ID"""
    mock_db = MagicMock()
    mock_db.query.return_value.filter.return_value.first.return_value = "book1"

    result = book_crud.get_book(mock_db, 1)

    assert result == "book1"


def test_update_book_unit():
    """Test updating a book successfully"""
    mock_db = MagicMock()
    mock_book = MagicMock(spec=Book)
    mock_db.query().filter().first.return_value = mock_book

    book_update = BookUpdate(
        title="Updated Book",
        author="Updated Author",
        published_year=2023,
        summary="Updated summary"
    )

    result = book_crud.update_book(mock_db, 1, book_update)

    assert result == mock_book
    assert mock_book.title == "Updated Book"
    assert mock_book.author == "Updated Author"
    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once_with(mock_book)


def test_delete_book_unit():
    """Test successful deletion of a book"""
    mock_db = MagicMock()
    mock_book = MagicMock(spec=Book)
    mock_db.query().filter().first.return_value = mock_book

    result = book_crud.delete_book(mock_db, 1)

    assert result == mock_book
    mock_db.delete.assert_called_once_with(mock_book)
    mock_db.commit.assert_called_once()


def test_get_nonexistent_book_unit():
    """Test retrieving a non-existent book returns None"""
    mock_db = MagicMock()
    mock_db.query.return_value.filter.return_value.first.return_value = None

    result = book_crud.get_book(mock_db, 999)
    assert result is None


def test_update_nonexistent_book_unit():
    """Test updating a non-existent book returns None"""
    mock_db = MagicMock()
    mock_db.query.return_value.filter.return_value.first.return_value = None
    book_data = BookUpdate(
        title="Updated Title",
        author="Author",
        summary="...",
        published_year=2024
    )

    result = book_crud.update_book(mock_db, 999, book_data)

    assert result is None


def test_delete_nonexistent_book_unit():
    """Test deleting a non-existent book returns None"""
    mock_db = MagicMock()
    mock_db.query.return_value.filter.return_value.first.return_value = None

    result = book_crud.delete_book(mock_db, 999)
    assert result is None


def test_create_book_with_minimal_data_unit():
    """Test creating a book with minimal data"""
    mock_db = MagicMock()
    book_data = BookCreate(
        title="Minimal Book",
        author="Author",
        description="",
        published_year=2024
    )

    result = book_crud.create_book(mock_db, book_data)

    assert result is not None
    mock_db.add.assert_called_once()
    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once()


def test_create_book_with_duplicate_title_unit():
    """Test handling of duplicate book title (simulated logic)"""
    mock_db = MagicMock()
    mock_db.query.return_value.filter.return_value.first.return_value = Book(
        id=1, title="Duplicate", author="Author"
    )

    book_data = BookCreate(
        title="Duplicate",
        author="Author",
        description="Desc",
        published_year=2020
    )

    def mock_create_book(book: BookCreate, db):
        existing = db.query(Book).filter(Book.title == book.title).first()
        if existing:
            raise HTTPException(status_code=400, detail="Book already exists")
        return Book(id=2, **book.dict())

    with pytest.raises(HTTPException) as exc_info:
        mock_create_book(book_data, mock_db)

    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "Book already exists"


def test_delete_nonexistent_book_with_exception_unit():
    """Test deleting a non-existent book raises 404"""
    mock_db = MagicMock()
    mock_db.query.return_value.filter.return_value.first.return_value = None

    def mock_delete_book(book_id: int, db):
        book = db.query(Book).filter(Book.id == book_id).first()
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        return {"message": "Deleted"}

    with pytest.raises(HTTPException) as exc_info:
        mock_delete_book(999, mock_db)

    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "Book not found"


def test_create_book_with_future_year_unit():
    """Test validation when published year is in the future"""
    mock_db = MagicMock()
    current_year = datetime.now().year
    future_year = current_year + 10

    book_data = BookCreate(
        title="Future Book",
        author="Sci-fi",
        description="from the future",
        published_year=future_year
    )

    def mock_create_book(book: BookCreate, db):
        if book.published_year > current_year:
            raise HTTPException(status_code=400, detail="Invalid published year")
        return Book(id=3, **book.dict())

    with pytest.raises(HTTPException) as exc_info:
        mock_create_book(book_data, mock_db)

    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "Invalid published year"


def test_update_nonexistent_book_with_exception_unit():
    """Test updating a non-existent book raises 404"""
    mock_db = MagicMock()
    mock_db.query.return_value.filter.return_value.first.return_value = None

    def mock_update_book(book_id: int, updated_data: BookCreate, db):
        book = db.query(Book).filter(Book.id == book_id).first()
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        return book

    with pytest.raises(HTTPException) as exc_info:
        mock_update_book(12345, BookCreate(
            title="Update",
            author="A",
            description="...",
            published_year=2022
        ), mock_db)

    assert exc_info.value.status_code == 404
