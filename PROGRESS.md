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
- [x] Verify Python syntax using `python -m compileall main.py com`.

### Pending Improvements
- [ ] Improve menu input validation so invalid choices show an error and let the user try again.
- [ ] Add automated tests for application logic.
- [ ] Test database-failure handling explicitly.

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

## Notes

- All five CRUD/search menu operations were run successfully after the environment-based database configuration and connection-handling changes.
- Database connection failures are now checked before attempting to create a cursor in each database method.
- SQL values are passed separately from query strings using parameterized queries.
- Keep the local `.env` file private and never commit it. Commit `.env.example` instead.
- If real database credentials were committed publicly in earlier commits, rotate them. Removing credentials in a later commit does not erase them from Git history.
