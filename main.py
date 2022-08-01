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

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1",port = 8080,reload=True) #,workers=2