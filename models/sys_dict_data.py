# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, String, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER
from models.model_base import Base


metadata = Base.metadata


class SysDictData(Base):
    __tablename__ = 'sys_dict_data'
    __table_args__ = {'comment': '字典数据表'}

    dictCode = Column('dict_code', BIGINT(20),primary_key=True, comment='字典编码')
    dictSort = Column('dict_sort', INTEGER(4),server_default=text("'0'"), comment='字典排序')
    dictLabel = Column('dict_label', String(100),server_default=text("''"), comment='字典标签')
    dictValue = Column('dict_value', String(100),server_default=text("''"), comment='字典键值')
    dictType = Column('dict_type', String(100),server_default=text("''"), comment='字典类型')
    cssClass = Column('css_class', String(100),comment='样式属性（其他样式扩展）')
    listClass = Column('list_class', String(100),comment='表格回显样式')
    isDefault = Column('is_default', CHAR(1),server_default=text("'N'"), comment='是否默认（Y是 N否）')
    status = Column(CHAR(1), server_default=text("'0'"), comment='状态（0正常 1停用）')
    createBy = Column('create_by', String(64),server_default=text("''"), comment='创建者')
    createTime = Column('create_time', DateTime,comment='创建时间')
    updateBy = Column('update_by', String(64),server_default=text("''"), comment='更新者')
    updateTime = Column('update_time', DateTime,comment='更新时间')
    remark = Column(String(500), comment='备注')
