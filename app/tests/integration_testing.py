"""
test_book_api.py

This module contains integration tests for the Book Catalog RESTful API using FastAPI's TestClient.
The tests cover the full CRUD functionality of the /books/ endpoints.

To run these tests:
    1. Ensure the application is importable and configured with a test database or mock environment.
    2. Use pytest or any other test runner.

Author: Samar Noor Riaz
"""

from fastapi.testclient import TestClient
from app.main import app

# Create a TestClient instance using the FastAPI app
client = TestClient(app)

def test_create_book():
    """
    Test the creation of a new book via POST /books/
    """
    response = client.post("/books/", json={
        "title": "Test Book",
        "author": "Author",
        "published_year": 2023,
        "summary": "Summary"
    })
    assert response.status_code == 200  # Successful creation
    assert response.json()["title"] == "Test Book"
    assert "id" in response.json()  # Ensure the book has an ID


def test_get_books():
    """
    Test retrieval of all books via GET /books/
    """
    response = client.get("/books/")
    assert response.status_code == 200  # Successful response
    assert isinstance(response.json(), list)  # Expecting a list of books


def test_get_book_by_id():
    """
    Test retrieving a specific book by ID via GET /books/{id}
    This test creates a new book first to ensure it exists.
    """
    create_response = client.post("/books/", json={
        "title": "Another Book",
        "author": "Tester",
        "published_year": 2022,
        "summary": "Test summary"
    })
    assert create_response.status_code == 200
    book_id = create_response.json()["id"]

    # Retrieve the created book by its ID
    response = client.get(f"/books/{book_id}")
    assert response.status_code == 200
    assert response.json()["id"] == book_id


def test_update_book():
    """
    Test updating a book via PUT /books/{id}
    This test creates a book first, then updates its data.
    """
    create_response = client.post("/books/", json={
        "title": "Old Title",
        "author": "Old Author",
        "published_year": 2021,
        "summary": "Old Summary"
    })
    assert create_response.status_code == 200
    book_id = create_response.json()["id"]

    # New data to update
    update_data = {
        "title": "New Title",
        "author": "New Author",
        "published_year": 2024,
        "summary": "Updated Summary"
    }

    # Perform update
    response = client.put(f"/books/{book_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["title"] == "New Title"


def test_delete_book():
    """
    Test deleting a book via DELETE /books/{id}
    This test creates a book, deletes it, and verifies it's gone.
    """
    create_response = client.post("/books/", json={
        "title": "To Delete",
        "author": "Author",
        "published_year": 2020,
        "summary": "To be deleted"
    })
    assert create_response.status_code == 200
    book_id = create_response.json()["id"]

    # Delete the book
    delete_response = client.delete(f"/books/{book_id}")
    assert delete_response.status_code == 200

    # Verify that the book is no longer retrievable
    get_response = client.get(f"/books/{book_id}")
    assert get_response.status_code == 404  # Not found
