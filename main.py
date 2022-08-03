from fastapi import FastAPI
import uvicorn
import api
import core

app = FastAPI()

# 注册中间件
core.register_middleware(app)

# 注册路由
api.add_routers(app)

@app.get("/")
async def index():
   
    return {"message": "Hello World From FastAPI"}

@app.get('/test/notice/{noticeId}')
def get_notice(noticeId: int):
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    from models.sys_notice import SysNotice

    engine = create_engine(core.Config.DB_URI)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()
    notice = session.query(SysNotice).filter(SysNotice.noticeId == noticeId).first()
    session.close()
    return notice

@app.get('/test/user/{userId}')
def get_notice(userId: int):
    from core.db_middleware import db
    from models.sys_user import SysUser

    session = db.session
    user = session.query(SysUser).filter(SysUser.userId == userId).first()
    return user

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1",port = 8080,reload=True) #,workers=2