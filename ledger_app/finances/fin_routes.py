from flask import Blueprint, render_template

fin = Blueprint('fin', __name__)

@fin.route('/')
def index():
    return render_template('index.html')