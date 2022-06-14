from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from aioredis import StrictRedis
from ratelimit.backends.redis import RedisBackend
from ratelimit import RateLimitMiddleware

from handlers import users, auth, home
from db.base import database
from error.error_limit import auth_error, blocked_error
from security.limited import credential_limit
from config import REDIS_HOST
from security.limited import config

app = FastAPI(title="Warpoint")

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(auth.router, prefix="/auth")
app.include_router(users.router, prefix="/user")
app.include_router(home.routing)
app.add_middleware(
    RateLimitMiddleware,
    authenticate=credential_limit,
    backend=RedisBackend(StrictRedis(host=REDIS_HOST)),
    config=config,
    on_auth_error=auth_error,
    on_blocked=blocked_error
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("app:app", host="0.0.0.0", port=5000)
