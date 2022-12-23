from datetime import timedelta


SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'

SECRET_KEY = b'6)\xba\xdf\x8euz\x00\x0f\xd7\xaa\xdb\xb4\x8a\xd4\xbe\x98\x1b\x84C\xcfR\xce9WL\xd1f\xd2\x16\x16\xe5'

STATIC_FOLDER = 'static'
TEMPLATE_FOLDER = 'templates'

JWT_SECRET_KEY = SECRET_KEY

JWT_EXPIRES = timedelta(hours=12)
JWT_IDENTITY_CLAIM = 'user'
JWT_HEADER_NAME = 'authorization'

PROPAGATE_EXCEPTIONS = True
