from sqlite3 import Cursor
from turtle import pos, title
from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode
from . import models, schemas
from .database import SessionLocal, engine, get_db
from .routers import  user, auth, poll


models.Base.metadata.create_all(bind = engine)
app = FastAPI()

while True:
    try:
        conn = psycopg2.connect(host= 'localhost', database='fastapi', user='postgres', password='1234', cursor_factory=RealDictCursor)
        cursor =conn.cursor()
        print("Database Connection was successfull")
        break
    except Exception as error:
        print("Connection to database failed")
        time.sleep(2)



app.include_router(poll.router)
app.include_router(user.router)
app.include_router(auth.router)