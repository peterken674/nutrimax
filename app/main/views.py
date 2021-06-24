from flask import render_template
from . import main
from .forms import FeedbackForm

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

@main.route('/about')
def about():
    form = FeedbackForm()
    title = 'About - Nutrimax'
    return render_template('about.html', title=title, form=form)

