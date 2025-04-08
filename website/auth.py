from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return '<h1>login</h1>'

@auth.route('/logout')
def logout():
    return '<h1>logout</h1>'

@auth.route('/signUp')
def signUp():
    return '<h1>signUp</h1>'

@auth.route('/signIn')
def signIn():
    return '<h1>signIn</h1>'