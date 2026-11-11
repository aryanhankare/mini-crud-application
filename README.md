# Mini CRUD Application

A command-line employee management application built with Python and MySQL. It supports creating, viewing, updating, deleting, and searching employee records.

This is a learning project focused on Python project structure, database connectivity, SQL, CRUD operations, and automated testing.

## Tech Stack

- Python 3.14+
- MySQL
- mysql-connector-python
- python-dotenv
- uv
- pytest

## Project Structure

```text
mini_crud_application/
├── com/
│   └── awm/
│       └── mini_app/
│           ├── controller/
│           ├── model/
│           └── util/
├── tests/
├── main.py
├── .env.example
├── pyproject.toml
├── uv.lock
└── PROGRESS.md
```

## Setup

1. Install Python 3.14 or later, MySQL, and [uv](https://docs.astral.sh/uv/).

2. Clone the repository:

   ```powershell
   git clone https://github.com/aryanhankare/mini-crud-application.git
   cd mini-crud-application
   ```

3. Install project dependencies:

   ```powershell
   uv sync
   ```

4. Create your local environment file from the example:

   ```powershell
   Copy-Item .env.example .env
   ```

5. Open `.env` and enter your own MySQL username, password, host, port, and database name. Create the database and the employee table expected by the application in MySQL before running it.

   The local `.env` file is ignored by Git. Do not commit your database credentials.

## Run the Application

```powershell
uv run python main.py
```

## Run Tests

```powershell
uv run python -m pytest -v
```

The automated tests use mocked database connections, so they do not require a running MySQL server.

## Current Features

- Display all employee records
- Create an employee
- Update an employee
- Delete an employee
- Search for an employee by ID
- Handle unavailable database connections
- Validate menu choices and non-integer menu input
- Use parameterized SQL queries
- Close database cursors and connections after operations

See [PROGRESS.md](PROGRESS.md) for completed work and planned improvements.
