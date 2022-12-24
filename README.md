# Todo API

## Frontend

### Development dependencies

- `prettier`: Formatter

## Backend

### Development workflow

- Run `eval (pdm venv activate in-project)` (if you are using Fish shell) or `eval $(pdm venv activate in-project)` (if you are using bash/zsh) at the `backend` folder root.

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

#### Difference between database schema and database model

- A schema defines the structure of data within the database.
- A model is a class that can be represented as rows in the database, i.e ID row, age row as class member.
