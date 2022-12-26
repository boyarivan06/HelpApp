from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from app.db_setup import SqlAlchemyBase
from werkzeug.security import generate_password_hash, check_password_hash


class HelpRequest(SqlAlchemyBase):
    __tablename__ = 'helprequests'
    id = Column(Integer, primary_key=True, autoincrement=True)
    author = Column(String, nullable=False)
    title = Column(String)
    text = Column(String)
    time_created = Column(DateTime, default=datetime.now())

    def __str__(self):
        return f'{self.author} at {self.time_created}'


class User(SqlAlchemyBase):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password_hash = Column(String, nullable=False, default='1234567890')
    time_created = Column(DateTime, default=datetime.now())
    admin = Column(Boolean, default=False)

    def change_password(self, new_password):
        self.password_hash = generate_password_hash(new_password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
