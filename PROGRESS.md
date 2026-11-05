# Project Progress

A simple record of what has been added to the Mini CRUD Application. Update this when a meaningful feature is completed.

## Current Status

- [x] Project structure created (controller, model, and util packages).
- [x] Employee model added.
- [x] MySQL connection helper added.
- [x] Display employee records implemented.
- [x] Create employee method added (latest update: 4 Nov 2026).
- [ ] Update employee functionality.
- [ ] Delete employee functionality.
- [ ] Connect the application properly through `main.py`.
- [ ] Move database credentials to environment variables.

## Progress Log

| Date | Progress |
| --- | --- |
| 3 Nov 2026 | Initial project structure and Python/MySQL setup pushed to GitHub. |
| 3 Nov 2026 | Added the project README. |
| 4 Nov 2026 | Added the create employee method with parameterized SQL, commit, and cursor/connection cleanup. |

## Notes

- The create employee code has been pushed, but it still needs to be tested with the database.
- Before calling the create method, check that the MySQL connection was successful.
- Keep database credentials out of source code and Git history; use environment variables.
- The update and delete menu options are not implemented yet.

