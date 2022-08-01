from fastapi import FastAPI
from .db_middleware import DBSessionMiddleware
from .config import Config

def register_middleware(app: FastAPI):
    app.add_middleware(DBSessionMiddleware, db_url=Config.DB_URI)
