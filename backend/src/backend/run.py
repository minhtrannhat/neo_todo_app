from quart import Quart, ResponseReturnValue

# Each blueprint is a logical collection of features in our web app
from backend.blueprints.control import blueprint as control_blueprint

# For making sure error responses are in JSON format
from backend.lib.api_error import APIError

# Rate limiting
from quart_rate_limiter import RateLimiter
from quart_rate_limiter import RateLimitExceeded
from datetime import timedelta

# Authentication
from quart_auth import AuthManager

# Request/Response validation
from quart_schema import QuartSchema, RequestSchemaValidationError


app: Quart = Quart(__name__)
auth_manager: AuthManager = AuthManager(app)
rate_limiter: RateLimiter = RateLimiter(app)
schema = QuartSchema(app, convert_casing=True)

# Configure the web app
# Either in DEV/DEBUG mode or TEST mode
app.config.from_prefixed_env(prefix="TODO")

app.register_blueprint(control_blueprint)


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
