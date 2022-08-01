# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, String, text,ForeignKey,Table
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.orm import relationship
from models.model_base import Base
from .sys_dept import SysDept
from .sys_role import SysRole
from .sys_post import SysPost

metadata = Base.metadata

sys_user_role = Table(
    'sys_user_role', metadata,
    Column('user_id', BIGINT(20),ForeignKey('sys_user.user_id'),primary_key=True, nullable=False, comment='用户ID'),
    Column('role_id', BIGINT(20),ForeignKey('sys_role.role_id'),primary_key=True, nullable=False, comment='角色ID' )
    )

sys_user_post = Table(
    'sys_user_post', metadata,
    Column('user_id', BIGINT(20),ForeignKey('sys_user.user_id'),primary_key=True, nullable=False, comment='用户ID'),
    Column('post_id', BIGINT(20),ForeignKey('sys_post.post_id'),primary_key=True, nullable=False, comment='岗位ID' )
    )

class SysUser(Base):
    __tablename__ = 'sys_user'
    __table_args__ = {'comment': '用户信息表'}

    userId = Column('user_id', BIGINT(20),primary_key=True, comment='用户ID')
    deptId = Column('dept_id', BIGINT(20),ForeignKey('sys_dept.dept_id'),comment='部门ID')
    userName = Column('user_name', String(30),nullable=False, comment='用户账号')
    nickName = Column('nick_name', String(30),nullable=False, comment='用户昵称')
    userType = Column('user_type', String(2),server_default=text("'00'"), comment='用户类型（00系统用户）')
    email = Column(String(50), server_default=text("''"), comment='用户邮箱')
    phonenumber = Column(String(11), server_default=text("''"), comment='手机号码')
    sex = Column(CHAR(1), server_default=text("'0'"), comment='用户性别（0男 1女 2未知）')
    avatar = Column(String(100), server_default=text("''"), comment='头像地址')
    password = Column(String(100), server_default=text("''"), comment='密码')
    status = Column(CHAR(1), server_default=text("'0'"), comment='帐号状态（0正常 1停用）')
    delFlag = Column('del_flag', CHAR(1),server_default=text("'0'"), comment='删除标志（0代表存在 2代表删除）')
    loginIp = Column('login_ip', String(128),server_default=text("''"), comment='最后登录IP')
    loginDate = Column('login_date', DateTime,comment='最后登录时间')
    createBy = Column('create_by', String(64),server_default=text("''"), comment='创建者')
    createTime = Column('create_time', DateTime,comment='创建时间')
    updateBy = Column('update_by', String(64),server_default=text("''"), comment='更新者')
    updateTime = Column('update_time', DateTime,comment='更新时间')
    remark = Column(String(500), comment='备注')

    dept = relationship('SysDept', backref='users',lazy="joined")
    roles = relationship('SysRole', secondary = 'sys_user_role',backref='user')
    posts = relationship('SysPost', secondary = 'sys_user_post',backref='user')

    @classmethod
    def isAdmin(cls, userId):
        return userId == 1
