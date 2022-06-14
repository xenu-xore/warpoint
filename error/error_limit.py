from fastapi.responses import JSONResponse
from ratelimit.types import ASGIApp


async def auth_error(exc: Exception) -> ASGIApp:
    return JSONResponse(
        {"message": "Срок жизни токена истек. Обратитесь к /auth"},
        status_code=403
    )


def blocked_error(retry_after: int) -> ASGIApp:
    return JSONResponse(
        {"message": "Вы превысили лимит запросов"},
        status_code=429
    )