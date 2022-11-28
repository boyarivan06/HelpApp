from flask import Flask, make_response, jsonify
from flask_jwt_simple import JWTManager
from flask_restful import Api
from app.resources.help_repo import MemoryHelpRepo
from app.tools.json_encoder import MyJsonEncoder
from app import db_setup


class HelpApp(Flask):
    def __init__(self, *args, **kwargs):
        super(HelpApp, self).__init__(*args, **kwargs)
        self.config.from_pyfile('config.py')

        db_setup.global_init('app/database.db')

        self.json_encoder = MyJsonEncoder
        self.help_repo = MemoryHelpRepo()
        self.jwt = JWTManager(self)
        self.api = Api(self)


app = HelpApp(__name__)


# (c) Jonny-programmer
@app.jwt.expired_token_loader
def expired_token_callback():
    err_json = {"message": "Expired token"}
    return make_response(jsonify(err_json), 401)  # Можно и 401

