
------------ Running Tests ------------------------
Run with pytest after installing dependencies:- 
-Make sure you are exactly in app folder
--Unit Tests: pytest tests/test_crud.py- 
--Integration Tests: pytest tests/test_routes.py- 
--All Tests: pytest

------------- Setup Instructions -------------------
1. Clone the repo:
   git clone https://github.com/Samar-Riaz/book-catalog.git
   cd book-catalog
 2. Create a virtual environment:
   python -m venv venv
   source venv/bin/activate  (Windows: venv\Scripts\activate)
 3. Install dependencies:
   pip install -r requirements.txt
4. Run the application:
   uvicorn app.main:app --reload
   Visit: http://127.0.0.1:8000/docs


---------------- Project Structure ----------------
book-catalog/
 ├── app/
 │   ├── main.py
 │   ├── models/
 │   ├── schemas/
 │   ├── crud/
 │   └── database/
 ├── tests/
 │   ├── test_crud.py
 │   └── test_routes.py
 ├── requirements.txt
 └── README.md

Author: Samar Noor Riaz
 Contributions: Fork, create a branch, commit changes, and open a pull request.
 For issues or feature suggestions: https://github.com/Samar-Riaz/book-catalog/issues