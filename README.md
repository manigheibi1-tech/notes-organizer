# Notes Organizer

A web-based academic notes organizer. Users can create courses and, within
each course, manage a collection of notes (title, description, content,
creation date). Notes are browsable through a collapsible tree view
(courses → notes) and searchable by title or content.

## Features

- User registration, login, and logout (with confirmation)
- Course management (create, edit, delete, list)
- Note management under each course (create, edit, delete, view)
- Text search across note titles and content
- Tree-style navigation (collapsible courses containing their notes)
- Per-user data isolation (each user only sees their own courses/notes)

## Tech Stack

- Backend: Django (MVT)
- Database: SQLite
- Frontend: Django templates + HTML/CSS

## Running Locally (without Docker)

1. Clone the repository:
```bash
   git clone https://github.com/manigheibi1-tech/notes-organizer.git
   cd notes-organizer
```

2. Install dependencies:
```bash
   pip install -r requirements.txt
```

3. Apply migrations:
```bash
   python manage.py migrate
```

4. Run the development server:
```bash
   python manage.py runserver
```

5. Open `http://127.0.0.1:8000` in your browser.

## Running with Docker

1. Make sure Docker Desktop is installed and running.

2. From the project root, build and start the container:
```bash
   docker compose up --build
```

3. Open `http://localhost:8000` in your browser.

4. To stop the container:
```bash
   docker compose down
```

## Running Tests

```bash
python manage.py test
```