from typing import Any
from sqlalchemy.ext.declarative import as_declarative
from utils.string_utils import snake_to_camel
'''
所有 model 类的基类
to-do: 用来扩展
'''
@as_declarative()
class Base:
    id: Any
    __name__: str

    def __repr__(self):
        '''以字典的形式，将数据转换为字符串'''
        # data_dict = {c.name: getattr(self, c.name, None) for c in self.__table__.columns} 
        return str(self.get_dict())

    def get_dict(self):
        '''将对象转化为字典'''
        of,tf = self.get_fields()
        data_dict = {attr_name: getattr(self, attr_name, None) for attr_name in of} 
        return data_dict

    @classmethod
    def get_fields(cls):
        '''获取类属性名与字段名'''
        table_fields = [c.name  for c in cls.__table__.columns]
        object_fields = [snake_to_camel(f) for f in table_fields]
        return object_fields, table_fields

    @classmethod
    def get_select_fields(cls,tf = '',alias = ''):
        '''根据字段名生成 SQL 的 select 字段 部分，
        避免生成对象时，对照错误
        '''
        if alias != '' and not alias.endswith('.'):
            alias += '.'
        if tf == '':
            tf = [c.name  for c in cls.__table__.columns]
        sf = ''.join([alias + f + ',' for f in tf])
        sf = sf[:-1]
        return sf