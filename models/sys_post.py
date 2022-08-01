# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, String, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER
from sqlalchemy.orm import relationship
from models.model_base import Base


metadata = Base.metadata


class SysPost(Base):
    __tablename__ = 'sys_post'
    __table_args__ = {'comment': '岗位信息表'}

    postId = Column('post_id', BIGINT(20),primary_key=True, comment='岗位ID')
    postCode = Column('post_code', String(64),nullable=False, comment='岗位编码')
    postName = Column('post_name', String(50),nullable=False, comment='岗位名称')
    postSort = Column('post_sort', INTEGER(4),nullable=False, comment='显示顺序')
    status = Column(CHAR(1), nullable=False, comment='状态（0正常 1停用）')
    createBy = Column('create_by', String(64),server_default=text("''"), comment='创建者')
    createTime = Column('create_time', DateTime,comment='创建时间')
    updateBy = Column('update_by', String(64),server_default=text("''"), comment='更新者')
    updateTime = Column('update_time', DateTime,comment='更新时间')
    remark = Column(String(500), comment='备注')

