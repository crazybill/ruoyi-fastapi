from typing import Union,List,Any
from pydantic import BaseModel
from models.sys_user import SysUser

class LoginForm(BaseModel):
    username: str
    password: str
    code: Union[str, None] = None
    uuid: Union[str, None] = None

class LoginUser(BaseModel):

    uid: str = '' # 用户唯一标识
    loginTime: float = 0 # 登陆时间
    visitTime: float = 0  # 上次刷新时间
    expireTime: float = 0  # 过期时间
    ipaddr: str = ''    # 登录IP地址
    loginLocation: str = '' #登录地点
    device: str = ''    # 设备
    browser: str = ''   # 浏览器类型
    os: str = ''        # 操作系统
    roles: Union[List, None] = None   # 角色列表
    permissions: Union[List, None] = None   # 权限列表
    user: Any = None    # 用户信息

    def getUserName(self):
        return self.user.userName

    def getPassword(self):
        return self.user.password

