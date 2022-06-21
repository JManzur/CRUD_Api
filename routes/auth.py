from fastapi import APIRouter, Header
from pydantic import BaseModel, EmailStr
from jwt_functions import validate_token, write_token
from fastapi.responses import JSONResponse

auth = APIRouter()

class User(BaseModel):
    username: str
    email: EmailStr

@auth.post("/login")
def login(user: User):
    print(user.dict())
    if user.username == "Jhonnathan":
        return write_token(user.dict())
    else:
        return JSONResponse(content={"message": "User not found"}, status_code=404)


@auth.post("/verify/token")
def verify_token(Authorization: str = Header(None)):
    token = Authorization.split(" ")[1]
    return validate_token(token, output=True)