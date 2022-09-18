from fastapi import APIRouter, Response, Header, Depends
from config.db import db_connection
from models.users import users_table
from starlette.status import HTTP_204_NO_CONTENT
from schemas.user import User
from middleware.verify_token import VerifyTokenRoute
from routes.auth import oauth2_scheme

crud = APIRouter(route_class=VerifyTokenRoute)

@crud.post("/create", tags=["Operations"])
def create(user: User, Authorization: str = Header(None), token: str = Depends(oauth2_scheme)):
    new_user = {
        "name": user.name,
        "last_name": user.last_name,
        "email": user.email
        }
    insert_operation = db_connection.execute(users_table.insert().values(new_user))
    create_result = db_connection.execute(users_table.select().where(users_table.c.id == insert_operation.lastrowid)).first()
    return create_result

@crud.get("/read", response_model=list[User], tags=["Operations"])
def read(Authorization: str = Header(None), token: str = Depends(oauth2_scheme)):
    return db_connection.execute(users_table.select()).fetchall()

@crud.get("/read/{id}", response_model=User, tags=["Operations"])
def read_id(id: str, Authorization: str = Header(None), token: str = Depends(oauth2_scheme)):
    return db_connection.execute(users_table.select().where(users_table.c.id == id)).first()

@crud.put("/update/{id}", response_model=User, tags=["Operations"])
def update_id(id: str, user: User, Authorization: str = Header(None), token: str = Depends(oauth2_scheme)):
    db_connection.execute(users_table.update().values(
        name = user.name,
        last_name = user.last_name,
        email = user.email
    ).where(users_table.c.id == id))
    return db_connection.execute(users_table.select().where(users_table.c.id == id)).first()

@crud.delete("/delete/{id}", status_code=HTTP_204_NO_CONTENT, tags=["Operations"])
def delete_id(id: str, Authorization: str = Header(None), token: str = Depends(oauth2_scheme)):
    db_connection.execute(users_table.delete().where(users_table.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)