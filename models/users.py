from tokenize import String
from sqlalchemy import Integer, Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

# Create MySQL Table:
users_table = Table("users", meta, 
    Column("id", Integer, primary_key=True), 
    Column("name", String(255)), 
    Column("last_name", String(255)),
    Column("email", String(255)))

meta.create_all(engine)