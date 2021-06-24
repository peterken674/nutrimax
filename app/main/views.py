from ..models import Total
from flask import render_template, flash
from flask.globals import request
from flask_login.utils import login_required
from werkzeug.utils import redirect
from . import main
from .forms import FeedbackForm, SearchBar
from ..email import mail_feedback
from flask_login import current_user
from ..requests import get_details

@main.route('/')
def index():
    '''View the index page.
    '''
    title = 'Home'
    return render_template('index.html', title=title)

@main.route('/info')
def info():
    '''View the search page.
    '''
    form = SearchBar()
    foods = get_details("3 burgers and fries and orange juice")

    nf_total_fat = 0.0
    nf_saturated_fat = 0.0
    nf_cholesterol = 0.0
    nf_sodium = 0.0
    nf_total_carbohydrates = 0.0
    nf_dietary_fiber = 0.0
    nf_sugars = 0.0
    nf_proteins = 0.0
    nf_potassium = 0.0


    for food in foods:
        if food.nf_total_fat:
            nf_total_fat += food.nf_total_fat
        if food.nf_saturated_fat:    
            nf_saturated_fat += food.nf_saturated_fat
        if food.nf_cholesterol: 
            nf_cholesterol += food.nf_cholesterol 
        if food.nf_sodium:
            nf_sodium += food.nf_sodium 
        if food.nf_total_carbohydrates:
            nf_total_carbohydrates += food.nf_total_carbohydrates
        if food.nf_dietary_fiber:
            nf_dietary_fiber += food.nf_dietary_fiber
        if food.nf_sugars:
            nf_sugars += food.nf_sugars
        if food.nf_proteins:
            nf_proteins += food.nf_proteins
        if food.nf_potassium:
            nf_potassium += food.nf_potassium

        totals = Total(nf_total_fat, nf_saturated_fat, nf_cholesterol, nf_sodium, nf_total_carbohydrates, nf_dietary_fiber, nf_sugars, nf_proteins, nf_potassium)

    title = 'Info | Nutrimax'
    return render_template('food_info.html', title=title, foods=foods, totals=totals, form=form)

@main.route('/about', methods=['GET', 'POST'])
def about():
    form = FeedbackForm()
    title = 'About | Nutrimax'

    
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
