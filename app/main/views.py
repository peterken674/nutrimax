from flask import render_template
from . import main


@main.route('/')
def index():
    '''View the index page.
    '''
    title = 'Home'
    return render_template('index.html', title=title)

@main.route('/info')
def info():
    '''View the index page.
    '''
    title = 'Info'
    return render_template('food_info.html', title=title)

@main.route('/login')
def login():
    '''View the login page.
    '''
    title = 'Login'
    return render_template('login.html', title=title)

@main.route('/signup')
def signup():
    '''View the signup page.
    '''
    title = 'Signup'
    return render_template('signup.html', title=title)

