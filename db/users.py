import sqlalchemy as sa
from db.base import metadata

Users = sa.Table(
    "users",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True, autoincrement=True, unique=True),
    sa.Column("email", sa.String, unique=True),
    sa.Column("hashed_password", sa.String),
    sa.Column("auth_token", sa.String),
)
