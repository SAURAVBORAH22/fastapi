from fastapi import FastAPI
import models
from database import engine

app = FastAPI()

# use database.py file and models.py file to create database
models.Base.metadata.create_all(bind=engine)