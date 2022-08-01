# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, String, text
from sqlalchemy.dialects.mysql import BIGINT
from models.model_base import Base


metadata = Base.metadata


class SysJobLog(Base):
    __tablename__ = 'sys_job_log'
    __table_args__ = {'comment': '定时任务调度日志表'}

    jobLogId = Column('job_log_id', BIGINT(20),primary_key=True, comment='任务日志ID')
    jobName = Column('job_name', String(64),nullable=False, comment='任务名称')
    jobGroup = Column('job_group', String(64),nullable=False, comment='任务组名')
    invokeTarget = Column('invoke_target', String(500),nullable=False, comment='调用目标字符串')
    jobMessage = Column('job_message', String(500),comment='日志信息')
    status = Column(CHAR(1), server_default=text("'0'"), comment='执行状态（0正常 1失败）')
    exceptionInfo = Column('exception_info', String(2000),server_default=text("''"), comment='异常信息')
    createTime = Column('create_time', DateTime,comment='创建时间')
