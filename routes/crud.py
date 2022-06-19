from fastapi import APIRouter, Response, status
from config.db import db_connection
from models.users import users_table
from starlette.status import HTTP_204_NO_CONTENT
from schemas.user import User
import logging

logger = logging.basicConfig(
	filename='crud_api.log',
	format='[%(asctime)s] %(levelname)s %(name)s %(message)s',
	level=logging.INFO,
	datefmt='%Y-%m-%d %H:%M:%S'
)

#Instanciate the API:
crud = APIRouter()

@crud.post("/create", tags=["Operations"])
def create(user: User):
    new_user = {
        "name": user.name,
        "last_name": user.last_name,
        "email": user.email
        }
    insert_operation = db_connection.execute(users_table.insert().values(new_user))
    create_result = db_connection.execute(users_table.select().where(users_table.c.id == insert_operation.lastrowid)).first()
    logging.info(create_result)
    return create_result

@crud.get("/read", response_model=list[User], tags=["Operations"])
def read():
    return db_connection.execute(users_table.select()).fetchall()

@crud.get("/read/{id}", response_model=User, tags=["Operations"])
def read_id(id: str):
    return db_connection.execute(users_table.select().where(users_table.c.id == id)).first()

@crud.put("/update/{id}", response_model=User, tags=["Operations"])
def update_id(id: str, user: User):
    db_connection.execute(users_table.update().values(
        name = user.name,
        last_name = user.last_name,
        email = user.email
    ).where(users_table.c.id == id))
    return db_connection.execute(users_table.select().where(users_table.c.id == id)).first()

@crud.delete("/delete/{id}", status_code=HTTP_204_NO_CONTENT, tags=["Operations"])
def delete_id(id: str):
    db_connection.execute(users_table.delete().where(users_table.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)