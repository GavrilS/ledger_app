from flask import Blueprint, render_template, request
from .user import User
# from ledger_app import db

auth = Blueprint('auth', __name__)

@auth.route('/login', method=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if not email or not password:
            raise Exception('User email and password are required to login...')
        #ToDo get user from db and open user ledgers page
        return render_template('user_ledgers.html')

    return render_template('login.html')

@auth.route('/signup', method=('GET', 'POST'))
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if not name or not email or not password:
            raise Exception('Please populate all fields...')
        if password != confirm_password:
            raise Exception('Password mismatch...')
        
        user = User(name=name, email=email, password=password)
        #ToDo add logic to save user to the DB
        return render_template('login.html')
    
    return render_template('signup.html')

@auth.route('/logout')
def logout():
    return render_template('index.html')