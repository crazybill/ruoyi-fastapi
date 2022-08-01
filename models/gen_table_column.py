# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, String, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER
from models.model_base import Base


metadata = Base.metadata


class GenTableColumn(Base):
    __tablename__ = 'gen_table_column'
    __table_args__ = {'comment': '代码生成业务表字段'}

    columnId = Column('column_id', BIGINT(20),primary_key=True, comment='编号')
    tableId = Column('table_id', String(64),comment='归属表编号')
    columnName = Column('column_name', String(200),comment='列名称')
    columnComment = Column('column_comment', String(500),comment='列描述')
    columnType = Column('column_type', String(100),comment='列类型')
    javaType = Column('java_type', String(500),comment='JAVA类型')
    javaField = Column('java_field', String(200),comment='JAVA字段名')
    isPk = Column('is_pk', CHAR(1),comment='是否主键（1是）')
    isIncrement = Column('is_increment', CHAR(1),comment='是否自增（1是）')
    isRequired = Column('is_required', CHAR(1),comment='是否必填（1是）')
    isInsert = Column('is_insert', CHAR(1),comment='是否为插入字段（1是）')
    isEdit = Column('is_edit', CHAR(1),comment='是否编辑字段（1是）')
    isList = Column('is_list', CHAR(1),comment='是否列表字段（1是）')
    isQuery = Column('is_query', CHAR(1),comment='是否查询字段（1是）')
    queryType = Column('query_type', String(200),server_default=text("'EQ'"), comment='查询方式（等于、不等于、大于、小于、范围）')
    htmlType = Column('html_type', String(200),comment='显示类型（文本框、文本域、下拉框、复选框、单选框、日期控件）')
    dictType = Column('dict_type', String(200),server_default=text("''"), comment='字典类型')
    sort = Column(INTEGER(11), comment='排序')
    createBy = Column('create_by', String(64),server_default=text("''"), comment='创建者')
    createTime = Column('create_time', DateTime,comment='创建时间')
    updateBy = Column('update_by', String(64),server_default=text("''"), comment='更新者')
    updateTime = Column('update_time', DateTime,comment='更新时间')
