from flask import render_template
from . import main

@main.route('/')
def index():
    '''View the index page.
    '''
    title = 'Home'
    return render_template('index.html', title=title)

@main.route('/register')
def register():
    '''View the register page.
    '''
    title = 'Register'
    return render_template('register.html', title=title)    