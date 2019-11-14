from flask import Blueprint

search = Blueprint('search', __name__)

# new archive api
@search.route('/')
def query():
    return '<h1>Hello, this is search archive page</h1>'
