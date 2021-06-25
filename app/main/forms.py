from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.fields.core import StringField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import Required

class FeedbackForm(FlaskForm):
    
    subject = StringField('', validators=[Required()], render_kw={'placeholder':'Subject'})
    feedback = TextAreaField('', validators=[Required()], render_kw={'placeholder':'Write us your feedback...'})
    
    submit = SubmitField('Send')

class SearchBar(FlaskForm):
    query = StringField('', validators=[Required()], render_kw={'placeholder':'Search for a meal...'})
    submit = SubmitField('Search')

    