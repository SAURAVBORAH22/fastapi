from fastapi import FastAPI
from routers import auth, todos, admin
import models
from database import engine

app = FastAPI()

# use database.py file and models.py file to create database
models.Base.metadata.create_all(bind=engine)

#including auth router and todos router to main file
app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)