# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, String, text
from sqlalchemy.dialects.mysql import BIGINT
from models.model_base import Base


metadata = Base.metadata


class SysDictType(Base):
    __tablename__ = 'sys_dict_type'
    __table_args__ = {'comment': '字典类型表'}

    dictId = Column('dict_id', BIGINT(20),primary_key=True, comment='字典主键')
    dictName = Column('dict_name', String(100),server_default=text("''"), comment='字典名称')
    dictType = Column('dict_type', String(100),unique=True, server_default=text("''"), comment='字典类型')
    status = Column(CHAR(1), server_default=text("'0'"), comment='状态（0正常 1停用）')
    createBy = Column('create_by', String(64),server_default=text("''"), comment='创建者')
    createTime = Column('create_time', DateTime,comment='创建时间')
    updateBy = Column('update_by', String(64),server_default=text("''"), comment='更新者')
    updateTime = Column('update_time', DateTime,comment='更新时间')
    remark = Column(String(500), comment='备注')
