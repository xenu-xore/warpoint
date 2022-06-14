from starlette.config import Config

config = Config(".env")

POSTGRES_USER=config("POSTGRES_USER", cast=str, default="")
POSTGRES_PASSWORD=config("POSTGRES_PASSWORD", cast=str, default="")
POSTGRES_DB=config("POSTGRES_DB", cast=str, default="")
POSTGRES_HOST=config("POSTGRES_HOST", cast=str, default="")
POSTGRES_PORT=config("POSTGRES_PORT", cast=str, default="")

REDIS_HOST = config("REDIS_HOST", cast=str, default="")

ACCESS_TOKEN_EXPIRE_MINUTES = 2
ALGORITHM = "HS256"
SECRET_KEY = config("SECRET_KEY", cast=str, default="")