from flask import Blueprint

fin = Blueprint('fin', __name__)

@fin.route('/')
def index():
    return 'Home page'