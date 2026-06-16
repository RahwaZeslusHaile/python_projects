# Job Application Tracker

A Flask web application for tracking job applications using **raw SQL (psycopg2)**, **PostgreSQL**, and a **SOLID layered architecture**.

This project is designed to demonstrate backend engineering fundamentals without relying on an ORM, focusing instead on clean architecture, SQL, and maintainable code structure.

---

## Project Goal

Help users manage their job search by tracking applications in one place.

Users can:

* Add job applications
* View all applications
* Update application status and details
* Delete applications

---

## MVP Features

* Create a job application
* View all applications
* Update an application
* Delete an application

---

## Application Fields

Each job application includes:

* Company name
* Job title
* Location
* Status
* Date applied
* Job link
* Notes

---

## Tech Stack

* Flask (web framework)
* PostgreSQL (database)
* psycopg2 (raw SQL driver)
* yoyo-migrations (SQL migrations)
* HTML templates (Jinja2)
* CSS (styling)

---

## Architecture (SOLID + Layered Design)

This project follows a clean layered architecture:

### Controllers (Flask Blueprints)

* Handle HTTP requests
* Validate input
* Call services
* Return responses/templates

### Services

* Contain business logic
* Enforce rules and validation
* Orchestrate repository calls

### Repositories

* Contain all raw SQL queries
* Handle database access only
* Return domain objects / DTOs

### Domain Models

* Represent core entities (JobApplication)
* Defined using dataclasses

### DTOs / Schemas (optional)

* Validate and structure data between layers

---

## Project Structure

```text
job-tracker/
│
├── app/
│   ├── __init__.py
│   │
│   ├── controllers/
│   │   └── job_controller.py
│   │
│   ├── services/
│   │   └── job_service.py
│   │
│   ├── repositories/
│   │   ├── job_repository.py
│   │   └── postgres_job_repository.py
│   │
│   ├── domain/
│   │   └── job_application.py
│   │
│   ├── db/
│   │   └── connection_pool.py
│   │
│   ├── templates/
│   └── static/
│
├── migrations/
├── tests/
├── run.py
├── requirements.txt
└── .env
```

---

## Database Setup (PostgreSQL)

### Install dependencies

```bash
pip install psycopg2-binary yoyo-migrations
```

### Environment variable

```bash
export DATABASE_URL='postgresql://jobuser:jobpass@localhost:5432/jobtracker'
```

---

## Database Migrations (yoyo)

Create migration:

```bash
yoyo new migrations "create job applications table"
```

Apply migrations:

```bash
yoyo apply --database "$DATABASE_URL" migrations
```

## Application Flow

1. User sends HTTP request
2. Controller receives request
3. Input is validated and mapped to a domain object
4. Service applies business rules
5. Repository executes SQL query
6. Database returns result
7. Service returns data to controller
8. Controller renders template or response

---

## Example Status Values

* Applied
* Interviewing
* Offer
* Rejected
* Archived

---

## Running the Project

### 1. Start PostgreSQL (Docker)

```bash
docker compose up -d
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run migrations

```bash
yoyo apply --database "$DATABASE_URL" migrations
```

### 4. Start Flask app

```bash
flask run --reload
```

---

## Testing Strategy

* Unit test **services** by mocking repositories
* Integration test repositories with a test Postgres database
* Run migrations before tests

---

## Security Best Practices

* Always use parameterized queries (`%s`)
* Never concatenate SQL strings
* Store credentials in environment variables
* Use least-privilege DB users

---

## Future Improvements

After MVP:

* Search and filtering
* Dashboard statistics
* Authentication (user accounts)
* Email reminders
* CSV export

---

## Design Philosophy

This project prioritizes:

* Clear separation of concerns
* Explicit SQL (no ORM abstraction)
* Testable service layer
* Scalable architecture
* Real-world backend structure

The goal is not just to build a CRUD app, but to demonstrate how production-style backend systems are structured.
