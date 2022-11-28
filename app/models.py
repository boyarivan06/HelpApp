from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from app.db_setup import SqlAlchemyBase


class HelpRequest(SqlAlchemyBase):
    __tablename__ = 'helprequests'
    id = Column(Integer, primary_key=True, autoincrement=True)
    author = Column(String, nullable=False)
    title = Column(String)
    text = Column(String)
    time_created = Column(DateTime, default=datetime.now())


