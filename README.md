# Book Management REST API

## Overview
A REST API built using Django and Django REST Framework to manage book records.

## Features
- Create a book
- Retrieve all books
- Retrieve a book by ID
- Update a book using PUT or PATCH
- Delete a book
- Validate incoming data

## Book Fields
- `id`: Automatically generated ID
- `title`: Book title
- `author`: Author name
- `price`: Book price
- `published_year`: Publication year

## Setup Instructions

1. Clone or download the repository.
2. Create and activate a virtual environment.
3. Install dependencies using `pip install -r requirements.txt`.
4. Run migrations using `python manage.py migrate`.
5. Start the server using `python manage.py runserver`.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/books/` | List books |
| POST | `/api/books/` | Create a book |
| GET | `/api/books/{id}/` | Retrieve a book |
| PUT | `/api/books/{id}/` | Update a book |
| PATCH | `/api/books/{id}/` | Partially update a book |
| DELETE | `/api/books/{id}/` | Delete a book |

## Technology Stack
- Python
- Django
- Django REST Framework
- SQLite
