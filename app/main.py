# from pydantic import typing
from fastapi import FastAPI

from .database import engine
from . import models, schemas
from .routers import employee, auth

# models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/")
def index():
    return {"data": "test"}


app.include_router(employee.router)
app.include_router(auth.router)
