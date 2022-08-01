from fastapi import FastAPI
from .db_middleware import DBSessionMiddleware
from .time_middleware import ProcessTimeMiddleWare
from .config import Config

def register_middleware(app: FastAPI):
    app.add_middleware(DBSessionMiddleware, db_url=Config.DB_URI)
    app.add_middleware(ProcessTimeMiddleWare)
