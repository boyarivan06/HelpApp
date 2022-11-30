from app.app_file import app
from flask_restful import Resource, reqparse, abort
from flask_jwt_simple import jwt_required, get_jwt_identity
from flask import jsonify, request as req
from app.models import HelpRequest


@app.route('/api/help_requests', methods=['GET', 'POST'])
def help_requests():
    if req.method == 'GET':
        requests = app.help_repo.get_all()
        return jsonify(requests)
    elif req.method == 'POST':
        request = HelpRequest(author=req.json['author'])


'''help_parser = reqparse.RequestParser()
help_parser.add_argument('id', required=True)
help_parser.add_argument('author', required=True)
help_parser.add_argument('title')
help_parser.add_argument('text')
help_parser.add_argument('time_created')


class HelpRes(Resource):
    def get(self, post_id):
        post = app.help_repo.get_by_id(post_id)
        print(post)
        return jsonify(post)

    # :@jwt_required
    def delete(self, id):
        result = app.help_repo.request_delete(id)
        if result:
            abort(400, message=result)
        return jsonify({"message": "success"})


class HelpListRes(Resource):
    def get(self, **kwargs):
        if "category_name" in kwargs:
            return jsonify(app.help_repo.get_by_category(kwargs["category_name"]))
        posts = app.help_repo.get_all()
        return jsonify(posts)

    # @jwt_required
    def post(self):
        args = help_parser.parse_args()
        post = HelpRequest(
            category=args.get('category', None),
            title=args.get('title', None),
            text=args.get('text', None),
            url=args.get('url', None),
            type=args.get('type', None),
        )
        print("~~~~This worked!~~~~")
        post = app.help_repo.request_create(post)
        return jsonify(post)


app.api.add_resource(HelpRes, '/api/help_request/<int:help_id>')
app.api.add_resource(HelpListRes, '/api/help_requests/')
'''

if __name__ == '__main__':
    app.run()