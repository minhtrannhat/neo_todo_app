from quart import Blueprint, ResponseReturnValue
from quart_rate_limiter import rate_exempt

blueprint = Blueprint("control", __name__)


@blueprint.get("/control/ping/")
@rate_exempt
async def ping() -> ResponseReturnValue:
    """Ping the server
    Check if server is up and running.
    """
    return {"ping": "pong"}
