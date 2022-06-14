from databases import Database
from sqlalchemy import create_engine, MetaData
from config import POSTGRES_DB, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_USER, POSTGRES_PORT

database_url = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
database = Database(database_url)
metadata = MetaData()
engine = create_engine(database_url)
