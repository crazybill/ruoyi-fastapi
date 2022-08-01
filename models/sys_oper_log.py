# coding: utf-8
from sqlalchemy import Column, DateTime, String, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER
from models.model_base import Base


metadata = Base.metadata


class SysOperLog(Base):
    __tablename__ = 'sys_oper_log'
    __table_args__ = {'comment': '操作日志记录'}

    operId = Column('oper_id', BIGINT(20),primary_key=True, comment='日志主键')
    title = Column(String(50), server_default=text("''"), comment='模块标题')
    businessType = Column('business_type', INTEGER(2),server_default=text("'0'"), comment='业务类型（0其它 1新增 2修改 3删除）')
    method = Column(String(100), server_default=text("''"), comment='方法名称')
    requestMethod = Column('request_method', String(10),server_default=text("''"), comment='请求方式')
    operatorType = Column('operator_type', INTEGER(1),server_default=text("'0'"), comment='操作类别（0其它 1后台用户 2手机端用户）')
    operName = Column('oper_name', String(50),server_default=text("''"), comment='操作人员')
    deptName = Column('dept_name', String(50),server_default=text("''"), comment='部门名称')
    operUrl = Column('oper_url', String(255),server_default=text("''"), comment='请求URL')
    operIp = Column('oper_ip', String(128),server_default=text("''"), comment='主机地址')
    operLocation = Column('oper_location', String(255),server_default=text("''"), comment='操作地点')
    operParam = Column('oper_param', String(2000),server_default=text("''"), comment='请求参数')
    jsonResult = Column('json_result', String(2000),server_default=text("''"), comment='返回参数')
    status = Column(INTEGER(1), server_default=text("'0'"), comment='操作状态（0正常 1异常）')
    errorMsg = Column('error_msg', String(2000),server_default=text("''"), comment='错误消息')
    operTime = Column('oper_time', DateTime,comment='操作时间')
