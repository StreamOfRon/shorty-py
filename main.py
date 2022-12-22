from asyncio import to_thread as asyncify
from configparser import ConfigParser

from fastapi import FastAPI, HTTPException

from datastore import get_datastore
from models import ShortURL

CONFIG_FILE="config.ini"

config = ConfigParser()
config.read(CONFIG_FILE)

app = FastAPI(
  docs_url=None,
  openapi_url=None,
  redoc_url=None
)

datastore = get_datastore(config)

@app.get("/")
async def root():
  return {"message": "Hello World"}

@app.get("/{shortened}")
async def get_shortened(shortened: str, edit: bool=False):
  return shortened

@app.get("/{shortened}/{argument}")
async def get_shortened_with_arg(shortened: str, argument: str):
  return f"{shortened}/{argument}"

@app.post("/")
async def create():
  pass

@app.put("/")
async def update():
  pass

@app.delete("/")
async def delete():
  pass

async def _get_shortened(shortened: str, argument: str=None):
  pass
