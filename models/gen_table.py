# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, String, text
from sqlalchemy.dialects.mysql import BIGINT
from models.model_base import Base


metadata = Base.metadata


class GenTable(Base):
    __tablename__ = 'gen_table'
    __table_args__ = {'comment': '代码生成业务表'}

    tableId = Column('table_id', BIGINT(20),primary_key=True, comment='编号')
    tableName = Column('table_name', String(200),server_default=text("''"), comment='表名称')
    tableComment = Column('table_comment', String(500),server_default=text("''"), comment='表描述')
    subTableName = Column('sub_table_name', String(64),comment='关联子表的表名')
    subTableFkName = Column('sub_table_fk_name', String(64),comment='子表关联的外键名')
    className = Column('class_name', String(100),server_default=text("''"), comment='实体类名称')
    tplCategory = Column('tpl_category', String(200),server_default=text("'crud'"), comment='使用的模板（crud单表操作 tree树表操作）')
    packageName = Column('package_name', String(100),comment='生成包路径')
    moduleName = Column('module_name', String(30),comment='生成模块名')
    businessName = Column('business_name', String(30),comment='生成业务名')
    functionName = Column('function_name', String(50),comment='生成功能名')
    functionAuthor = Column('function_author', String(50),comment='生成功能作者')
    genType = Column('gen_type', CHAR(1),server_default=text("'0'"), comment='生成代码方式（0zip压缩包 1自定义路径）')
    genPath = Column('gen_path', String(200),server_default=text("'/'"), comment='生成路径（不填默认项目路径）')
    options = Column(String(1000), comment='其它生成选项')
    createBy = Column('create_by', String(64),server_default=text("''"), comment='创建者')
    createTime = Column('create_time', DateTime,comment='创建时间')
    updateBy = Column('update_by', String(64),server_default=text("''"), comment='更新者')
    updateTime = Column('update_time', DateTime,comment='更新时间')
    remark = Column(String(500), comment='备注')
