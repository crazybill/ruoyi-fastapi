# coding: utf-8
from itertools import permutations
from sqlalchemy import CHAR, Column, DateTime, String, text,Table,ForeignKey
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, TINYINT
from sqlalchemy.orm import relationship
from models.model_base import Base


metadata = Base.metadata

sys_role_menu = Table(
    'sys_role_menu', metadata,
    Column('role_id', BIGINT(20),ForeignKey('sys_role.role_id'),primary_key=True, nullable=False, comment='角色ID'),
    Column('menu_id', BIGINT(20),ForeignKey('sys_menu.menu_id'),primary_key=True, nullable=False, comment='菜单ID')
)

class SysRole(Base):
    __tablename__ = 'sys_role'
    __table_args__ = {'comment': '角色信息表'}

    roleId = Column('role_id', BIGINT(20),primary_key=True, comment='角色ID')
    roleName = Column('role_name', String(30),nullable=False, comment='角色名称')
    roleKey = Column('role_key', String(100),nullable=False, comment='角色权限字符串')
    roleSort = Column('role_sort', INTEGER(4),nullable=False, comment='显示顺序')
    dataScope = Column('data_scope', CHAR(1),server_default=text("'1'"), comment='数据范围（1：全部数据权限 2：自定数据权限 3：本部门数据权限 4：本部门及以下数据权限）')
    menuCheckStrictly = Column('menu_check_strictly', TINYINT(1),server_default=text("'1'"), comment='菜单树选择项是否关联显示')
    deptCheckStrictly = Column('dept_check_strictly', TINYINT(1),server_default=text("'1'"), comment='部门树选择项是否关联显示')
    status = Column(CHAR(1), nullable=False, comment='角色状态（0正常 1停用）')
    delFlag = Column('del_flag', CHAR(1),server_default=text("'0'"), comment='删除标志（0代表存在 2代表删除）')
    createBy = Column('create_by', String(64),server_default=text("''"), comment='创建者')
    createTime = Column('create_time', DateTime,comment='创建时间')
    updateBy = Column('update_by', String(64),server_default=text("''"), comment='更新者')
    updateTime = Column('update_time', DateTime,comment='更新时间')
    remark = Column(String(500), comment='备注')

    # 关联属性
    menus = relationship('SysMenu', secondary=sys_role_menu, backref='role')
