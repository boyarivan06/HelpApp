from datetime import timedelta


SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'

SECRET_KEY = ''

STATIC_FOLDER = 'static'
TEMPLATE_FOLDER = 'templates'

JWT_SECRET_KEY = SECRET_KEY

JWT_EXPIRES = timedelta(hours=12)
JWT_IDENTITY_CLAIM = 'user'
JWT_HEADER_NAME = 'authorization'

PROPAGATE_EXCEPTIONS = True
