from app.app_file import app
from flask_restful import Resource, reqparse, abort
from flask_jwt_simple import jwt_required, get_jwt_identity
from flask import jsonify, request as req, render_template
from app.models import HelpRequest
from flask import Response
from app.forms import HelpForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = HelpForm()
    if form.validate_on_submit() or req.method == 'POST':
        app.help_repo.request_create(HelpRequest(author='testing-testing...'))
        print('.........HELP..........')
        print(jsonify(app.help_repo.get_all()).json)
    return render_template('index.html')


@app.route('/admin')
def admin():
    data = app.help_repo.get_all()
    return render_template('admin.html', data=data)


@app.route('/api/help_requests', methods=['GET', 'POST'])
def help_requests():
    if req.method == 'GET':
        requests = app.help_repo.get_all()
        answer = jsonify(requests)
        print(answer.json)
        return 'is it works?'
    elif req.method == 'POST':
        request = HelpRequest(author=req.json['author'])
        app.help_repo.request_create(request)
        return jsonify(request)


if __name__ == '__main__':
    app.run()