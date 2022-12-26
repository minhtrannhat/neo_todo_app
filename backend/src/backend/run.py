# logging
import logging
import os
from subprocess import call  # nosec
from urllib.parse import urlparse

from quart import Quart, ResponseReturnValue

# Authentication
from quart_auth import AuthManager

# PostgreSQL database driver
from quart_db import QuartDB

# Rate limiting
from quart_rate_limiter import RateLimiter, RateLimitExceeded

# Request/Response validation
from quart_schema import QuartSchema, RequestSchemaValidationError

# Each blueprint is a logical collection of features in our web app
from backend.blueprints.control import blueprint as control_blueprint
from backend.blueprints.members import blueprint as members_blueprint
from backend.blueprints.sessions import blueprint as sessions_blueprint

# For making sure error responses are in JSON format
from backend.lib.api_error import APIError

app: Quart = Quart(__name__)

# Configure the web app
# Either in DEV/DEBUG mode or TEST mode
app.config.from_prefixed_env(prefix="TODO")

auth_manager: AuthManager = AuthManager(app)
quart_db = QuartDB(app)
rate_limiter: RateLimiter = RateLimiter(app)
schema = QuartSchema(app, convert_casing=True)
logging.basicConfig(level=logging.INFO)

# registers these groups of routes handlers
app.register_blueprint(control_blueprint)
app.register_blueprint(sessions_blueprint)
app.register_blueprint(members_blueprint)


# rate limiting
@app.errorhandler(RateLimitExceeded)  # type: ignore
async def handle_rate_limit_exceeded_error(
    error: RateLimitExceeded,
) -> ResponseReturnValue:
    return {}, error.get_headers(), 429


# handles errors
@app.errorhandler(APIError)  # type: ignore
async def handle_api_error(error: APIError) -> ResponseReturnValue:
    return {"code": error.code}, error.status_code


@app.errorhandler(500)
async def handle_generic_error(error: Exception) -> ResponseReturnValue:
    return {"code": "INTERNAL_SERVER_ERROR"}, 500


# Schema validation error handler
@app.errorhandler(RequestSchemaValidationError)  # type: ignore
async def handle_request_validation_error(
    error: RequestSchemaValidationError,
) -> ResponseReturnValue:
    if isinstance(error.validation_error, TypeError):
        return {"errors": str(error.validation_error)}, 400
    else:
        return {"errors": error.validation_error.json()}, 400


@app.cli.command("recreate_db")
def recreate_db() -> None:
    db_url = urlparse(os.environ["TODO_QUART_DB_DATABASE_URL"])
    call(  # nosec
        [
            "psql",
            "-U",
            "postgres",
            "-c",
            f"DROP DATABASE IF EXISTS {db_url.path.removeprefix('/')}",
        ],
    )
    call(  # nosec
        ["psql", "-U", "postgres", "-c", f"DROP USER IF EXISTS {db_url.username}"],
    )
    call(  # nosec
        [
            "psql",
            "-U",
            "postgres",
            "-c",
            f"CREATE USER {db_url.username} LOGIN PASSWORD '{db_url.password}' CREATEDB",  # noqa: E501
        ],
    )
    call(  # nosec
        [
            "psql",
            "-U",
            "postgres",
            "-c",
            f"CREATE DATABASE {db_url.path.removeprefix('/')}",
        ],
    )
