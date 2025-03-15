from flask import Blueprint, render_template, request
from .user import User
# from ledger_app import db

auth = Blueprint('auth', __name__)

@auth.route('/login', method=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        pass #ToDo get user from db and open user ledgers page
    
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/logout')
def logout():
    return render_template('index.html')