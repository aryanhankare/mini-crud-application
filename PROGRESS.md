# Project Progress

A running record of completed features, improvements, and next steps for the Mini CRUD Application.

## Current Status

### Completed
- [x] Project structure created with controller, model, and utility packages.
- [x] Employee model implemented.
- [x] MySQL connection helper created.
- [x] Display all employee records (Read).
- [x] Add employee records (Create) using parameterized SQL.
- [x] Update employee records using parameterized SQL.
- [x] Delete employee records using parameterized SQL.
- [x] Connect the application through `main.py` as the entry point.
- [x] Search for an employee by ID using a parameterized SELECT query and `fetchone()`.
- [x] Move database credentials into environment variables using `python-dotenv`.
- [x] Add `.env.example` as a safe configuration template.
- [x] Update `.gitignore` to exclude local environment files and other unnecessary files.
- [x] Remove the module-level connection call so importing the MySQL utility module does not open a database connection.
- [x] Handle failed database connections consistently in all CRUD and search methods.
- [x] Run all menu options successfully after the connection-handling changes.
- [x] Add menu input validation for non-integer input and invalid menu choices.
- [x] Add `pytest` as a development dependency.
- [x] Add automated tests for menu behavior and database operations using mocks.
- [x] Test database-failure handling explicitly without requiring a live database.
- [x] Verify Python syntax using `python -m compileall main.py com`.
- [x] Run the automated test suite successfully: **6 tests passed** using `uv run python -m pytest -v`.

### Pending Improvements
- [ ] Add tests for employee update, deletion, and search operations.
- [ ] Add tests for not-found cases and invalid employee IDs.
- [ ] Improve validation for blank employee fields and non-positive IDs.
- [ ] Review repeated database connection and cleanup code for a possible refactor.
- [ ] Improve the README with setup, configuration, and testing instructions.

## Progress Log

| Date | Progress |
| --- | --- |
| 3 Nov 2026 | Created the initial Python project structure and configured the MySQL setup. |
| 3 Nov 2026 | Added the project README. |
| 4 Nov 2026 | Implemented employee creation with parameterized SQL, transaction commit, and cursor/connection cleanup. |
| 5 Nov 2026 | Implemented employee update and deletion with parameterized SQL, transaction commits, and cursor/connection cleanup. |
| 6 Nov 2026 | Connected the application through `main.py`, making it the main entry point instead of starting the menu during controller import. |
| 6 Nov 2026 | Added employee search by ID using a parameterized SELECT query and `fetchone()`. |
| 8 Nov 2026 | Moved MySQL credentials into environment variables using `python-dotenv`, added `.env.example`, updated `.gitignore`, and removed the automatic connection call during module import. |
| 8 Nov 2026 | Verified that the application connects to MySQL and displays employee records using the new environment-based configuration. |
| 9 Nov 2026 | Added consistent database connection checks to all five CRUD/search methods, compiled the Python files successfully, and tested all menu options. |
| 10 Nov 2026 | Added menu input validation and introduced `pytest` for automated testing. |
| 10 Nov 2026 | Added six tests covering menu input, menu dispatch, employee creation, unavailable database handling, and fetching employee records. All six tests passed. |

## Notes

- The current automated tests use mocked database connections, so they do not need a running MySQL server.
- Run the test suite with `uv run python -m pytest -v`.
- Use `uv run python -m pytest -v` rather than `uv run pytest -v` in this project so the project root is available for imports.
- Database connection failures are checked before attempting to create a cursor in each database method.
- SQL values are passed separately from query strings using parameterized queries.
- Keep the local `.env` file private and never commit it. Commit `.env.example` instead.
- If real database credentials were committed publicly in earlier commits, rotate them. Removing credentials in a later commit does not erase them from Git history.
