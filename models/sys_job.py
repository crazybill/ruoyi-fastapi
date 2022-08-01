# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, String, text
from sqlalchemy.dialects.mysql import BIGINT
from models.model_base import Base


metadata = Base.metadata


class SysJob(Base):
    __tablename__ = 'sys_job'
    __table_args__ = {'comment': '定时任务调度表'}

    jobId = Column('job_id', BIGINT(20),primary_key=True, nullable=False, comment='任务ID')
    jobName = Column('job_name', String(64),primary_key=True, nullable=False, server_default=text("''"), comment='任务名称')
    jobGroup = Column('job_group', String(64),primary_key=True, nullable=False, server_default=text("'DEFAULT'"), comment='任务组名')
    invokeTarget = Column('invoke_target', String(500),nullable=False, comment='调用目标字符串')
    cronExpression = Column('cron_expression', String(255),server_default=text("''"), comment='cron执行表达式')
    misfirePolicy = Column('misfire_policy', String(20),server_default=text("'3'"), comment='计划执行错误策略（1立即执行 2执行一次 3放弃执行）')
    concurrent = Column(CHAR(1), server_default=text("'1'"), comment='是否并发执行（0允许 1禁止）')
    status = Column(CHAR(1), server_default=text("'0'"), comment='状态（0正常 1暂停）')
    createBy = Column('create_by', String(64),server_default=text("''"), comment='创建者')
    createTime = Column('create_time', DateTime,comment='创建时间')
    updateBy = Column('update_by', String(64),server_default=text("''"), comment='更新者')
    updateTime = Column('update_time', DateTime,comment='更新时间')
    remark = Column(String(500), server_default=text("''"), comment='备注信息')
