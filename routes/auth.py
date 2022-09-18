from fastapi import APIRouter, Header, Depends
from pydantic import BaseModel, EmailStr
from config.jwt_functions import validate_token, write_token
from fastapi.responses import JSONResponse
from config.db import collection
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

auth = APIRouter()

class User(BaseModel):
    username: EmailStr
    password: str

@auth.post("/login", tags=["Authentication"])
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    mongodb_query = collection.find_one({'username':'{}'.format(form_data.username)})
    try:
        if form_data.username == mongodb_query['username'] and form_data.password == mongodb_query['password']:
            user_dict = {'username': '{}'.format(form_data.username)}
            return write_token(user_dict)
        else:
            return JSONResponse(content={"Message": "User not found or invalid credentials"}, status_code=404)
    except TypeError:
        return JSONResponse(content={"Message": "TypeError Exception Raised"}, status_code=500)

@auth.post("/verify/token", tags=["Authentication"])
def verify_token(Authorization: str = Header(None), token: str = Depends(oauth2_scheme)):
    token = Authorization.split(" ")[1]
    return validate_token(token, output=True)