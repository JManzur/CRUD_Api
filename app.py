from fastapi import FastAPI, status
from fastapi.staticfiles import StaticFiles
from routes.crud import crud
from routes.auth import auth
from dotenv import load_dotenv
import logging

logger = logging.basicConfig(
	filename='/usr/src/app/crud_api.log',
    #filename='crud_api.log',
	format='[%(asctime)s] %(levelname)s %(name)s %(message)s',
	level=logging.INFO,
	datefmt='%Y-%m-%d %H:%M:%S'
)

description = """
CRUD API Using FastAPI
"""

app = FastAPI(
    openapi_tags=[{
        "name": "Operations",
        "description": "CRUD Operations on Users Table"
    }],
    title="CRUD Api",
    description=description,
    version="0.0.1",
    contact={
        "name": "JManzur",
        "url": "https://jmanzur.com"
        },
)

app.include_router(crud)
app.include_router(auth)
load_dotenv()

app.mount("/", StaticFiles(directory="landing_page", html=True), name="landing_page")

@app.get("/", status_code=200)
async def home():
    return {}

@app.get('/healthcheck', status_code=status.HTTP_200_OK)
def perform_healthcheck():
    return {'healthcheck': 'Everything OK!'}