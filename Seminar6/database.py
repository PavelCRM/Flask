import databases
import sqlalchemy

DATABASE_URL = "sqlite:///./shop.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, index=True),
    sqlalchemy.Column("first_name", sqlalchemy.String, index=True),
    sqlalchemy.Column("last_name", sqlalchemy.String, index=True),
    sqlalchemy.Column("email", sqlalchemy.String, unique=True, index=True),
    sqlalchemy.Column("password", sqlalchemy.String),
)

items = sqlalchemy.Table(
    "items",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, index=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("description", sqlalchemy.String),
    sqlalchemy.Column("price", sqlalchemy.Float),
)

orders = sqlalchemy.Table(
    "orders",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, index=True),
    sqlalchemy.Column("user_id", None, sqlalchemy.ForeignKey("users.id")),
    sqlalchemy.Column("item_id", None, sqlalchemy.ForeignKey("items.id")),
    sqlalchemy.Column("order_date", sqlalchemy.String),
    sqlalchemy.Column("status", sqlalchemy.String),
)
