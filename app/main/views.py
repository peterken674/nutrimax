from flask import render_template
from . import main


@main.route('/')
def index():
    '''View the index page.
    '''
    title = 'Home'
    return render_template('index.html', title=title)
@main.route('/login')
def login():
    '''View the login page.
    '''
    title = 'Login'
    return render_template('login.html', title=title)