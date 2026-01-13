from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = os.getenv("SECRET_KEY")

from auth_routes import auth_router
from order_routes import order_router

app = FastAPI()


app.include_router(auth_router)
app.include_router(order_router)

