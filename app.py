from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.crud import crud
from routes.auth import auth
from dotenv import load_dotenv
from fastapi.responses import JSONResponse
from starlette.status import HTTP_200_OK
import socket

description = """
CRUD API Using FastAPI
"""

app = FastAPI(
    openapi_tags=[
        {
            "name": "Operations",
            "description": "CRUD Operations on Users Table"
        },
        {
            "name": "Authentication",
            "description": "Endpoints for user authentication"
        },
        {
            "name": "HealthCheck",
            "description": "Endpoint to validate availability, and system information"
        }
    ],
    title="CRUD Api",
    description=description,
    version="0.0.1",
    contact={
        "name": "JManzur",
        "url": "https://jmanzur.com"
        },
)

hostname = (socket.gethostname())

app.include_router(crud)
app.include_router(auth)
load_dotenv()

@app.get("/healthcheck", status_code=HTTP_200_OK, tags=["HealthCheck"])
async def healthcheck():
    return JSONResponse(content={
        "Healthy": True,
        "StatusCode": HTTP_200_OK,
        "Host": "{}".format(hostname)
        })

app.mount("/", StaticFiles(directory="landing_page", html=True), name="landing_page")