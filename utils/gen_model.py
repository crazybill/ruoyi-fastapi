import os
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy.ext.declarative import declarative_base
from string_utils import snake_to_camel


class Config:
    # 数据库
    HOST = 'localhost'
    PORT = '3306'
    DATABASE = 'ruoyi'
    USERNAME = 'ruoyi'
    PASSWORD = 'admin'

    DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD, host=HOST,port=PORT, db=DATABASE)

def change_columns(filename):
    lines = []
    with open(filename,'r',encoding='utf-8') as f:
        for line in f.readlines():
            if 'sqlalchemy.ext.declarative' in line:
                line = 'from models.model_base import Base'
            elif 'declarative_base()' in line:
                line = ''
            elif 'Column(' in line:
                line = line[4:]
                parts = line.split()
                if '_' in parts[0]:
                    fname = snake_to_camel(parts[0])
                    cname = parts[2]
                    cname = cname.replace('Column(',"Column('"+parts[0]+"', ")
                    line = fname +' = ' + cname + ' '.join(parts[3:])
                line = '    '+line

            if not line.endswith('\n'):
                line += '\n'
            lines.append(line)
    with open(filename,'w',encoding='utf-8') as f:
        f.writelines(lines)

def gen(table_name):
    tables = f'--tables {table_name}'
    model_filename = f'models/{table_name}.py'
    if not os.path.exists(model_filename):
        print('正在生成  ',os.path.abspath(model_filename))
        os.system(f'sqlacodegen {Config.DB_URI} {tables} --outfile {model_filename}')
        change_columns(model_filename)
        print('生成完毕  ')

def gen_all():

    engine = create_engine(Config.DB_URI)
    session = sessionmaker(bind=engine)
    Base = declarative_base()
    Base.metadata.reflect(engine)
    tables = Base.metadata.tables  
    for table_name in tables:
        gen(table_name) 

if __name__ == '__main__':
    # gen('sys_user')
    gen_all()

