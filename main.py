from app.app_file import app
from flask_restful import Resource, reqparse, abort
from flask_jwt_simple import jwt_required, get_jwt_identity
from flask import jsonify, request as req, render_template, redirect, url_for
from app.models import HelpRequest, User
from flask import Response
from app.forms import HelpForm, DeleteForm, RegisterForm, LoginForm
import datetime
import socket
from string import ascii_lowercase, ascii_uppercase, digits


requests_today = None
current_user = None


def password_valid(password: str):
    return len(password) >= 8 and (set(ascii_lowercase) & set(password) and (set(ascii_uppercase) & set(password))
                                   and (set(digits) & set(password)))


@app.route('/', methods=['GET', 'POST'])
def index():
    form = HelpForm()
    if form.validate_on_submit() or req.method == 'POST':
        if form.id.data == 0:
            new = HelpRequest(author=socket.gethostname())
            app.help_repo.request_create(new)
            return redirect(url_for('index'))
        elif form.id.data == 1:
            app.user_repo.make_admin(current_user.id)
    return render_template('index.html', user=current_user)


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if not current_user or not current_user.admin:
        return redirect(url_for('index'))
    form = DeleteForm()
    if form.validate_on_submit() or req.method == 'POST':
        app.help_repo.request_delete(form.id.data)
    data = app.help_repo.get_all()
    return render_template('admin.html', data=data, user=current_user)


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


@app.route('/reg', methods=['GET', 'POST'])
def register():
    global current_user
    form = RegisterForm()
    if form.validate_on_submit() or req.method == 'POST':
        if form.password.data != form.password_repeat.data:
            return render_template('reg.html', warning='Пароли не совпадают')
        if not password_valid(form.password.data):
            return render_template('reg.html', warning='Пароль ненадёжен')
        user = User(name=form.name.data, surname=form.surname.data, username=form.username.data)
        user.change_password(form.password.data)
        app.user_repo.request_create(user)
        current_user = user
        if user.admin:
            return redirect(url_for('admin'))
        return redirect(url_for('index'))
    else:
        return render_template('reg.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    global current_user
    form = LoginForm()
    if form.validate_on_submit() or req.method == 'POST':
        user = app.user_repo.get_by_username(form.username.data)
        if not user:
            return render_template('login.html', warning=f'Пользователя @{form.username.data} не существует')
        elif not user.check_password(form.password.data):
            return render_template('login.html', warning='Неверный пароль')
        current_user = user
        if user.admin:
            return redirect(url_for('admin'))
        return redirect(url_for('index'))
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    global current_user
    current_user = None
    return redirect(url_for('index'))


@app.route('/profile/<int:id>')
def profile(id):
    if id != current_user.id:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
