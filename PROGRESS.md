# Project Progress

A running record of completed features, improvements, and next steps for the Mini CRUD Application.

## Current Status

### Completed
- [x] Project structure created with controller, model, and utility packages.
- [x] Employee model implemented.
- [x] MySQL connection helper created.
- [x] Employee CRUD operations implemented: create, read, update, and delete.
- [x] Search employee by ID implemented.
- [x] SQL values passed through parameterized queries.
- [x] MySQL credentials moved to environment variables using `python-dotenv`.
- [x] Added `.env.example` and configured `.gitignore` to keep local environment files private.
- [x] Removed the module-level database connection so importing the utility module does not connect automatically.
- [x] Added handling for unavailable database connections.
- [x] Added menu input validation for non-integer input and invalid choices.
- [x] Added `pytest` as a development dependency.
- [x] Added automated tests using mocked database connections.
- [x] Added tests for create, read, update, delete, search, not-found behavior, menu dispatch, and unavailable database handling.
- [x] Refactored the employee controller to reuse connection, cleanup, and employee-display methods.
- [x] Verified the test suite: **11 tests passed** using `uv run python -m pytest -v`.

### Pending Improvements
- [ ] Add tests for update-not-found and invalid employee IDs.
- [ ] Add tests for database errors during SQL execution.
- [ ] Validate blank employee fields and non-positive IDs.
- [ ] Improve README setup, database configuration, and test instructions.
- [ ] Consider integration tests using a separate test database.

## Progress Log

| Date | Progress |
| --- | --- |
| 3 Nov 2026 | Created the initial Python project structure and configured the MySQL setup. |
| 3 Nov 2026 | Added the project README. |
| 4 Nov 2026 | Implemented employee creation with parameterized SQL, transaction commit, and cursor/connection cleanup. |
| 5 Nov 2026 | Implemented employee update and deletion with parameterized SQL, transaction commits, and cursor/connection cleanup. |
| 6 Nov 2026 | Connected the application through `main.py` and added employee search by ID. |
| 8 Nov 2026 | Moved MySQL credentials into environment variables, added `.env.example`, updated `.gitignore`, and removed the automatic connection call during module import. |
| 9 Nov 2026 | Added consistent database connection checks to all CRUD/search methods and tested the menu options. |
| 10 Nov 2026 | Added menu input validation and introduced `pytest` for automated testing. |
| 11 Nov 2026 | Expanded the automated test suite to 11 tests covering CRUD operations, search, and not-found cases. |
| 11 Nov 2026 | Refactored the controller to reuse database connection, resource cleanup, and employee display methods. All 11 tests passed. |

## Notes

- Tests use mocked database connections, so the test suite does not require a running MySQL server.
- Run tests with `uv run python -m pytest -v`.
- Use `uv run python -m pytest -v` rather than `uv run pytest -v` in this project so the project root is available for imports.
- SQL values are passed separately from query strings using parameterized queries.
- Keep the local `.env` file private and never commit it. Commit `.env.example` instead.
- Removing credentials in a later commit does not erase them from Git history. Rotate any credentials that may have been exposed in earlier commits.
