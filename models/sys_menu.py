# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, String, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER
from models.model_base import Base


metadata = Base.metadata


class SysMenu(Base):
    __tablename__ = 'sys_menu'
    __table_args__ = {'comment': '菜单权限表'}

    menuId = Column('menu_id', BIGINT(20),primary_key=True, comment='菜单ID')
    menuName = Column('menu_name', String(50),nullable=False, comment='菜单名称')
    parentId = Column('parent_id', BIGINT(20),server_default=text("'0'"), comment='父菜单ID')
    orderNum = Column('order_num', INTEGER(4),server_default=text("'0'"), comment='显示顺序')
    path = Column(String(200), server_default=text("''"), comment='路由地址')
    component = Column(String(255), comment='组件路径')
    query = Column(String(255), comment='路由参数')
    isFrame = Column('is_frame', INTEGER(1),server_default=text("'1'"), comment='是否为外链（0是 1否）')
    isCache = Column('is_cache', INTEGER(1),server_default=text("'0'"), comment='是否缓存（0缓存 1不缓存）')
    menuType = Column('menu_type', CHAR(1),server_default=text("''"), comment='菜单类型（M目录 C菜单 F按钮）')
    visible = Column(CHAR(1), server_default=text("'0'"), comment='菜单状态（0显示 1隐藏）')
    status = Column(CHAR(1), server_default=text("'0'"), comment='菜单状态（0正常 1停用）')
    perms = Column(String(100), comment='权限标识')
    icon = Column(String(100), server_default=text("'#'"), comment='菜单图标')
    createBy = Column('create_by', String(64),server_default=text("''"), comment='创建者')
    createTime = Column('create_time', DateTime,comment='创建时间')
    updateBy = Column('update_by', String(64),server_default=text("''"), comment='更新者')
    updateTime = Column('update_time', DateTime,comment='更新时间')
    remark = Column(String(500), server_default=text("''"), comment='备注')

    children = None
