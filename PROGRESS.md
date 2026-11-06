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

### Pending Improvements
- [ ] Move database credentials into environment variables and keep the `.env` file out of Git.
- [ ] Remove the standalone connection call from the MySQL utility module so importing it does not open an unnecessary database connection.
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

## Notes

- The existing Create, Read, Update, and Delete operations have been tested with the MySQL database.
- Employee search by ID has been added; test it with both an existing ID and a non-existent ID.
- SQL values are passed separately from query strings using parameterized queries.
- Database credentials are currently configured in the connection helper. Move them to environment variables before sharing or deploying the project.
- Keep secrets out of source code and Git history. Adding `.env` to `.gitignore` prevents future accidental commits, but does not erase credentials already present in Git history.
