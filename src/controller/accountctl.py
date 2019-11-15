from flask import Blueprint, request, jsonify
from model import Error, LoginSuccess
from service import sessionStore

account = Blueprint('account', __name__)

# user login api
@account.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == "" or password == "":
        return jsonify(Error("Input is empty"))
    
    cookie = sessionStore.login(username, password)
    if cookie == "":
        return jsonify(Error("Mismatch"))

    return jsonify(LoginSuccess(cookie))

# modify account info api (use post method)
@account.route('/remake')
def remake():
    return '<h1>Hello, this is account remake</h1>'