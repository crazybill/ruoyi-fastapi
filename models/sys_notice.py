# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, String, text
from sqlalchemy.dialects.mysql import INTEGER, LONGBLOB,LONGTEXT
from models.model_base import Base


metadata = Base.metadata


class SysNotice(Base):
    __tablename__ = 'sys_notice'
    __table_args__ = {'comment': '通知公告表'}

    noticeId = Column('notice_id', INTEGER(4),primary_key=True, comment='公告ID')
    noticeTitle = Column('notice_title', String(50),nullable=False, comment='公告标题')
    noticeType = Column('notice_type', CHAR(1),nullable=False, comment='公告类型（1通知 2公告）')
    noticeContent = Column('notice_content', LONGTEXT,comment='公告内容')
    status = Column(CHAR(1), server_default=text("'0'"), comment='公告状态（0正常 1关闭）')
    createBy = Column('create_by', String(64),server_default=text("''"), comment='创建者')
    createTime = Column('create_time', DateTime,comment='创建时间')
    updateBy = Column('update_by', String(64),server_default=text("''"), comment='更新者')
    updateTime = Column('update_time', DateTime,comment='更新时间')
    remark = Column(String(255), comment='备注')
