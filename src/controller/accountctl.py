from flask import Blueprint

account = Blueprint('account', __name__)

# user login api
@account.route('/login')
def login():
    return '<h1>Hello, this is login</h1>'

# modify account info api (use post method)
@account.route('/remake')
def remake():
    return '<h1>Hello, this is account remake</h1>'