from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    String,
    Table,
    create_engine
)
from databases import Database

SQLALCHEMY_DATABASE_URL = "mysql://root:@localhost/fastdb_2"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
metadata = MetaData()

Users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, unique=True, index=True),
    Column("username", String(30), unique=True),
    Column("roles", String(10)),
    Column("password", String(200))
)

database = Database(SQLALCHEMY_DATABASE_URL)
