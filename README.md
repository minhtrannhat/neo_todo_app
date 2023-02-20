# Todo API

## Frontend

### Development Workflow

- Format, lint and test with `npm run {format, lint, test}`.

### Dependencies

- React
- React helment async: manage changes to document head.
- Material UI
- Roboto font

## Backend

### Development Workflow

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
