# 📚 FastAPI Book Catalog

A simple CRUD-based Book Catalog API built with **FastAPI**, **SQLAlchemy**, and **Pydantic**.

---

## 🛠 Setup Instructions

```bash
# Clone the repository
git clone https://github.com/Samar-Riaz/book-catalog.git
cd book-catalog

# Create and activate a virtual environment
python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### ▶️ Run the Application

```bash
uvicorn app.main:app --reload
```

Open your browser and visit:  
👉 http://127.0.0.1:8000/docs  
for the interactive Swagger UI.

---

## ✅ Running Tests

After installing dependencies, use `pytest` to run tests.

> 📍 **Note:** Make sure you're in the **project root folder**, not inside `/app`.

```bash
# Run unit tests only
pytest tests/test_crud.py

# Run integration tests only
pytest tests/test_routes.py

# Run all tests
pytest
```

---

## 📁 Project Structure

```
book-catalog/
├── app/
│   ├── main.py           # FastAPI app entrypoint
│   ├── models.py         # SQLAlchemy models
│   ├── schemas.py        # Pydantic schemas
│   ├── crud.py           # CRUD operations
│   └── database.py       # DB setup
│
├── tests/
│   ├── test_crud.py      # Unit tests
│   └── test_routes.py    # Integration tests
│
├── requirements.txt      # Dependency list
└── README.md             # This file
```

---

## 👤 Author

**Samar Noor Riaz**

---

## 🤝 Contributions

Want to contribute?

- Fork the repo
- Create a new branch
- Commit your changes
- Push and open a Pull Request

Issues or feature suggestions?  
📬 Submit them here: [https://github.com/Samar-Riaz/book-catalog/issues](https://github.com/Samar-Riaz/book-catalog/issues)
