# MEL Django Project

A Django project with REST API capabilities.

## Requirements

- Python 3.11
- Django 4.2.20
- Django REST Framework 3.15.2
- Requests 2.32.3

## Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd MEL
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows:
     ```
     .\venv\Scripts\activate.bat
     ```
   - Linux/Mac:
     ```
     source venv/bin/activate
     ```

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Run migrations:
   ```
   python manage.py migrate
   ```

6. Create a superuser (optional):
   ```
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

8. Access the application at http://127.0.0.1:8000/

## Project Structure

- `MEL/` - Django project settings
- `manage.py` - Django management script 