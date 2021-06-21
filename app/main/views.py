from flask import render_template
from . import main

@main.route('/')
def index():
    '''View the index page.
    '''
    title = 'Home'
    return render_template('index.html', title=title)

@main.route('/contact')
def contact():
    '''View the contact page.
    '''
    title = 'Contact Us'
    return render_template('contact.html', title=title)