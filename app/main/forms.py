from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import Required

class FeedbackForm(FlaskForm):
    
    feedback = TextAreaField('', validators=[Required()], render_kw={'placeholder':'Write us your feedback...'})
    
    submit = SubmitField('Send')
    