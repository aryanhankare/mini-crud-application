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

### Pending Improvements
- [ ] Test all CRUD and search operations after the database configuration changes.
- [ ] Handle failed database connections consistently in every CRUD/search method.
- [ ] Improve menu input validation so invalid choices show an error and let the user try again.
- [ ] Add automated tests for application logic.

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

## Notes

- The existing Create, Read, Update, and Delete operations were tested before the database configuration changes.
- After moving credentials into `.env`, the application successfully connected to MySQL and displayed employee records. Full regression testing of all CRUD and search operations after this change is still pending.
- SQL values are passed separately from query strings using parameterized queries.
- Keep the local `.env` file private and never commit it. Commit `.env.example` instead.
- If real database credentials were committed publicly in earlier commits, rotate them. Removing credentials in a later commit does not erase them from Git history.
