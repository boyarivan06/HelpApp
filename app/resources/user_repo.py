from app.models import User
from app.db_setup import create_session
from datetime import datetime


class MemoryUsersRepo:
    def __init__(self):
        self.db_sess = create_session()

    def get_all(self):
        return self.db_sess.query(User).all()

    def get_by_id(self, id):
        user = self.db_sess.query(User).filter(User.id == id).first()
        return user

    def get_by_username(self, username):
        user = self.db_sess.query(User).filter(User.username == username).first()
        print("got user by name:", user)
        return user

    def request_create(self, new_user: User):
        user = self.get_by_id(new_user.id)
        if user:
            return None  # Пользователь с таким именем уже есть
        self.db_sess.add(new_user)
        self.db_sess.commit()
        return new_user

    def request_update(self, id, username, name, surname, email, password):
        user = self.db_sess.query(User).get(id)
        user.username = username
        user.name = name
        user.surname = surname
        user.email = email
        user.set_password(password)
        self.db_sess.add(user)
        self.db_sess.commit()

    def request_delete(self, id):
        self.db_sess.query(User).get(id).delete()
        self.db_sess.commit()

    def make_admin(self, id):
        user = self.db_sess.query(User).get(id)
        user.admin = True
        self.db_sess.add(user)
        self.db_sess.commit()
