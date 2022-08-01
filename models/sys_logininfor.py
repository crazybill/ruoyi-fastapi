# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, String, text
from sqlalchemy.dialects.mysql import BIGINT
from models.model_base import Base


metadata = Base.metadata


class SysLogininfor(Base):
    __tablename__ = 'sys_logininfor'
    __table_args__ = {'comment': '系统访问记录'}

    infoId = Column('info_id', BIGINT(20),primary_key=True, comment='访问ID')
    userName = Column('user_name', String(50),server_default=text("''"), comment='用户账号')
    ipaddr = Column(String(128), server_default=text("''"), comment='登录IP地址')
    loginLocation = Column('login_location', String(255),server_default=text("''"), comment='登录地点')
    browser = Column(String(50), server_default=text("''"), comment='浏览器类型')
    os = Column(String(50), server_default=text("''"), comment='操作系统')
    status = Column(CHAR(1), server_default=text("'0'"), comment='登录状态（0成功 1失败）')
    msg = Column(String(255), server_default=text("''"), comment='提示消息')
    loginTime = Column('login_time', DateTime,comment='访问时间')
