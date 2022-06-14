from ratelimit import Rule
from ratelimit.types import Scope
from fastapi.security.utils import get_authorization_scheme_param

from security.credentials import decode_access_token
from depends.collector import UsersCollector, get_user_collector


config = {
        r"^/$": [Rule(minute=60, group="default"), Rule(group="auth")],
    }


async def credential_limit(scope: Scope):
    users: UsersCollector = await get_user_collector()
    authorization = dict(scope["headers"]).get(b"authorization")

    if authorization:
        scheme, token = get_authorization_scheme_param(authorization.decode("utf-8"))

        if scheme.lower() != "bearer":
            raise

        if token:
            payload_token = decode_access_token(token)
            if payload_token is None:
                raise
            email: str = payload_token.get("sub")
            if email is None:
                raise
            user = await users.get_by_email(email=email)
            if user is None:
                raise

            return "127.0.0.1", "auth"

    return "127.0.0.1", "default"
