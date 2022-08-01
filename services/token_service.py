import time
from datetime import datetime, timedelta
from typing import Any, Union
from jose import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session
import uuid
from schemas.login_user import LoginUser
from models.sys_user import SysUser
from core.config import Config
from core.exceptions import *


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
ALGORITHM = "HS256"

class TokenService:

    async def login(self,db:Session,username:str,password:str,code:str='',uuid:str=''):
        '''用户登录验证，并生成 token，缓存 loginUser'''
        user = db.query(SysUser).filter(SysUser.userName == username)

        loginUser = LoginUser(user=user)
        roles = 'admin'
        permissions = '*:*:*'
        loginUser.roles = roles
        loginUser.permissions = permissions
        token = await self.create_token(loginUser)

        return token

    async def logout(self):
        '''退出登录，清除缓存里的 loginUser'''
        pass
        
    def get_payload(self,token: str) -> dict:
        '''从 token 中获取 payload'''
        pass

    async def create_token(self,loginUser: LoginUser):
        '''细化 loginUser 信息，返回 jwt token'''
        loginUser.uid = str(uuid.uuid4())
        loginUser.loginTime = time.time()
        loginUser.visitTime = loginUser.loginTime
        loginUser.expireTime = loginUser.visitTime + Config.ACCESS_TOKEN_EXPIRE_MINUTES * 60

        self.set_user_agent(loginUser)
        await self.refresh_token(loginUser)

        token = self.create_access_token(loginUser.uid)
        
        return token

    def set_user_agent(self,loginUser: LoginUser):
        '''从 request 中获取用户相关信息'''
        pass

    async def check_token(self,loginUser: LoginUser):
        '''检查 token 是否过期，距离过期时间小于 10 分钟则刷新 token'''
        if loginUser.expireTime - time.time() < 10*60:
            await self.refresh_token(loginUser)


    def create_access_token(
        self,
        subject: Union[str, Any], expires_delta: timedelta = None
    ) -> str:
        '''创建 jwt token'''
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(
                minutes=Config.USER_TOKEN_EXPIRE_MINUTES     # 用户浏览器保存的 token 过期时间
            )
        to_encode = {"exp": expire, "sub": str(subject)}
        encoded_jwt = jwt.encode(to_encode, Config.TOKEN_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    async def refresh_token(self,loginUser: LoginUser):
        '''刷新缓存里的 loginUser 的过期时间'''
        pass


tokenService = TokenService()


