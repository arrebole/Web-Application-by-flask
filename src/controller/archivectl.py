from flask import Blueprint

archive = Blueprint('archive', __name__)

# new archive api
@archive.route('/new')
def new():
    return '<h1>Hello, this is new archive page</h1>'


# modify archive
@archive.route('/remake/<int:id>')
def remake(id: int):
    return f'<h1>Hello, this is  modify archive {id} page</h1>'


# delete archive api
@archive.route('/delete/<int:id>')
def delete(id: int):
    return f'<h1>Hello, this is delete {id} archive page</h1>'