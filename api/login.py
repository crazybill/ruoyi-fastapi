from fastapi import APIRouter,Request
from schemas.login_user import LoginForm,LoginUser
from services import tokenService
from core.db_middleware import db

router = APIRouter(tags=['系统安全'])

@router.post('/login')
async def login(login_data: LoginForm):
    token = await tokenService.login(
        db.session,
        login_data.username,
        login_data.password,
        login_data.code,
        login_data.uuid)
    return {'token':token}

@router.get('/getInfo')
async def get_info(req: Request):
    result = {
        "user": {},
        "roles": {},
        "permissions": {},
        "loginUser": {}
    }
    return result

@router.get('/getRouters')
async def get_routers(req: Request):
    data = {}
    return {'data':data}

@router.get('/logout')
async def logout():
    await tokenService.logout()
    return {"msg":'退出成功'}

@router.post('/logout')
async def logout():
    await tokenService.logout()
    return {"msg":'退出成功'}