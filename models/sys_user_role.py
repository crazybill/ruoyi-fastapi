# coding: utf-8
from sqlalchemy import Column,ForeignKey
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.orm import relationship
from models.model_base import Base

metadata = Base.metadata


class SysUserRole(Base):
    __tablename__ = 'sys_user_role'
    __table_args__ = {'comment': '用户和角色关联表','extend_existing': True}

    userId = Column('user_id', BIGINT(20),ForeignKey('sys_user.user_id'),primary_key=True, nullable=False, comment='用户ID')
    roleId = Column('role_id', BIGINT(20),ForeignKey('sys_role.role_id'),primary_key=True, nullable=False, comment='角色ID' )

