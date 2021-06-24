from flask import render_template, flash
from flask.globals import request
from flask_login.utils import login_required
from werkzeug.utils import redirect
from . import main
from .forms import FeedbackForm
from ..email import mail_feedback
from flask_login import current_user

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

@main.route('/about', methods=['GET', 'POST'])
def about():
    form = FeedbackForm()
    title = 'About - Nutrimax'

    
    if form.validate_on_submit():
        if current_user.is_authenticated:
            # sender = current_user
            feedback = form.feedback.data 
            subject = form.subject.data
            

            mail_feedback(subject, feedback, 'feedback@gmail.com')
            return redirect(request.referrer)
        else:
            flash('Please log in first to submit feedback.')

    return render_template('about.html', title=title, form=form)
