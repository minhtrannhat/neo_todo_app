# Todo API

## Frontend

### Development dependencies

- `prettier`: Formatter

## Backend

### Development workflow

- Depends on the state of the database, run `pdm run recreate-db` to regenerate database.
- Run `eval (pdm venv activate in-project)` (if you are using Fish shell) or `eval $(pdm venv activate in-project)` (if you are using bash/zsh) at the `backend` folder root to get into the backend python virtual environment.
- Run tests, lints, formats with `pdm run {test, lint, format}`.

### Dependencies

#### Python dependencies

- `quart`: a micro-webframework, async version of Flask.
- `black`: Code formatter.
- `isort`: Import formatter.
- `mypy`: Type checking.
- `flake8`: General Python bugs.
- `vulture`: Find unused code in Python programs.
- `pytest`: For testing (turbocharged with `async`).
- `bcrypt`: Hashing and salting password.
- `zxcvbn`: Test password strength.
- `freezegun`: Check for expired token.
- `quart-rate-limiter`: Rate limiting.
- `pydantic` and `quart-schema`: Request/Response validation.
- `httpx`: send HTTP POST requests from our app.

#### SQL Dev-deps

- `bandit`: Check for SQL injection vulnerabilities.

#### Miscs Dev-deps

- `djhtml`: Generate jinja templates html for emails.

### Backend Technical Write-up

#### Quart specific terminologies

`blueprint`: a collection of route handlers/API functionalities.

#### API route trailing slashes

API paths should end with a slash i.e: `/sessions/` rather than `/session`.
This is because requests sent to `/sessions` will be redirected to `/sessions/` whereas `/sessions/` won't get redirected.

#### Difference between database schema and database model

- A schema defines the structure of data within the database.
- A model is a class that can be represented as rows in the database, i.e ID row, age row as class member.

#### Managing user's sessions (Authentication)

- Login should results in a cookie being set in the user's browser, which is being sent in every subsequent request.
  The presence and value of this cookie are used to determine whether the member is logged in, and which member made the request.
- Logout results in the cookie being deleted.

#### Idempotent routes

Idempotence is a property of a route where the final state is achieved no matter how many times the route is called, that is, calling the route once or 10 times has the same effect. This is a useful property as it means the route can be safely retried if the request fails. For RESTful and HTTP APIs, the routes using GET, PUT, and DELETE verbs are expected to be idempotent.
