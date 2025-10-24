QuerySet Django project (minimal)
=================================

Instructions to run locally:

1. Create and activate a virtual environment (recommended):
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # mac / linux:
   source venv/bin/activate

2. Install requirements:
   pip install -r requirements.txt

3. Apply migrations:
   python manage.py migrate

4. (Optional) Load sample books data:
   python manage.py loaddata books.json

5. Create a superuser to access admin:
   python manage.py createsuperuser

6. Run the development server:
   python manage.py runserver

Open http://127.0.0.1:8000/ for the books page and http://127.0.0.1:8000/admin/ for admin.

Notes:
- If you want the sample data to exist automatically, run step 4 after migrations.
- The DB is empty by default; fixtures/books.json contains five example books.
