# coding: utf-8
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT
from models.model_base import Base


metadata = Base.metadata


class SysRoleDept(Base):
    __tablename__ = 'sys_role_dept'
    __table_args__ = {'comment': '角色和部门关联表'}

    roleId = Column('role_id', BIGINT(20),primary_key=True, nullable=False, comment='角色ID')
    deptId = Column('dept_id', BIGINT(20),primary_key=True, nullable=False, comment='部门ID')
