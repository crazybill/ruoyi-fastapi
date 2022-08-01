# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, String, text
from sqlalchemy.dialects.mysql import INTEGER
from models.model_base import Base


metadata = Base.metadata


class SysConfig(Base):
    __tablename__ = 'sys_config'
    __table_args__ = {'comment': '参数配置表'}

    configId = Column('config_id', INTEGER(5),primary_key=True, comment='参数主键')
    configName = Column('config_name', String(100),server_default=text("''"), comment='参数名称')
    configKey = Column('config_key', String(100),server_default=text("''"), comment='参数键名')
    configValue = Column('config_value', String(500),server_default=text("''"), comment='参数键值')
    configType = Column('config_type', CHAR(1),server_default=text("'N'"), comment='系统内置（Y是 N否）')
    createBy = Column('create_by', String(64),server_default=text("''"), comment='创建者')
    createTime = Column('create_time', DateTime,comment='创建时间')
    updateBy = Column('update_by', String(64),server_default=text("''"), comment='更新者')
    updateTime = Column('update_time', DateTime,comment='更新时间')
    remark = Column(String(500), comment='备注')
