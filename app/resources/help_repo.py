from datetime import datetime
from app.db_setup import create_session
from app.models import HelpRequest


class MemoryHelpRepo:
    def __init__(self):
        self.session = create_session()

    def get_all(self):
        return tuple(self.session.query(HelpRequest).all())

    def get_by_id(self, id):
        post = self.session.query(HelpRequest).filter(HelpRequest.id == id).first()
        return post

    def request_create(self, help):
        # help.created = datetime.now()
        self.session.add(help)
        self.session.commit()
        return help

    def request_delete(self, help_id):
        post = self.session.query(HelpRequest).filter(HelpRequest.id == help_id).first()
        if not post:
            return f"Request does not exist for id {help_id}"
        self.session.delete(post)
        self.session.commit()
        return None

    '''def get_by_username(self, username):
        user = self.db_sess.query(User).filter(User.username == username).first()
        posts = self.db_sess.query(Post).filter(Post.author == user).all()
        return tuple(posts)'''

    '''def get_by_category(self, category):
        posts = self.db_sess.query(Post).filter(Post.category == category).all()
        return tuple(posts)'''
