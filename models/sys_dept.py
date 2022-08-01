# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, String, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER
from sqlalchemy.orm import relationship
from models.model_base import Base


metadata = Base.metadata


class SysDept(Base):
    __tablename__ = 'sys_dept'
    __table_args__ = {'comment': '部门表'}

    deptId = Column('dept_id', BIGINT(20),primary_key=True, comment='部门id')
    parentId = Column('parent_id', BIGINT(20),server_default=text("'0'"), comment='父部门id')
    ancestors = Column(String(50), server_default=text("''"), comment='祖级列表')
    deptName = Column('dept_name', String(30),server_default=text("''"), comment='部门名称')
    orderNum = Column('order_num', INTEGER(4),server_default=text("'0'"), comment='显示顺序')
    leader = Column(String(20), comment='负责人')
    phone = Column(String(11), comment='联系电话')
    email = Column(String(50), comment='邮箱')
    status = Column(CHAR(1), server_default=text("'0'"), comment='部门状态（0正常 1停用）')
    delFlag = Column('del_flag', CHAR(1),server_default=text("'0'"), comment='删除标志（0代表存在 2代表删除）')
    createBy = Column('create_by', String(64),server_default=text("''"), comment='创建者')
    createTime = Column('create_time', DateTime,comment='创建时间')
    updateBy = Column('update_by', String(64),server_default=text("''"), comment='更新者')
    updateTime = Column('update_time', DateTime,comment='更新时间')

    children = None
