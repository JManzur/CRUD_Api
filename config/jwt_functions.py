from jwt import encode, decode
from jwt import exceptions
from datetime import datetime, timedelta
from os import getenv
from dotenv import load_dotenv
from fastapi.responses import JSONResponse

load_dotenv()

def expire_date(timeframe: int):
    expiration = datetime.utcnow() + timedelta(minutes=timeframe)
    return expiration

def write_token(data: dict):
    token = encode(payload={**data, "exp": expire_date(30) }, key=getenv("JWT_SECRET"), algorithm="HS256")
    return JSONResponse(content={
        "access_token": token,
        "token_type": "bearer"
        })

def validate_token(token, output=False):
    try:
        if output:
            return decode(token, key=getenv("JWT_SECRET"), algorithms=["HS256"])
        decode(token, key=getenv("JWT_SECRET"), algorithms=["HS256"])
    except exceptions.DecodeError:
        return JSONResponse(content={"message": "Invalid Token"}, status_code=401)
    except exceptions.ExpiredSignatureError:
        return JSONResponse(content={"message": "Token Expired"}, status_code=401)