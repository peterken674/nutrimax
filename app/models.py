from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin
from . import login_manager
from sqlalchemy import desc


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

    
class User(UserMixin, db.Model):
    '''Class to define a user of the application.
    '''
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    fname = db.Column(db.String(255))
    lname = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute.')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'

class Food:
    '''Class to define the food details received from the API response.
    '''

    def __init__(self, food_name, brand_name, serving_qty, serving_unit, serving_weight_grams, nf_calories, nf_total_fat, nf_saturated_fat, nf_cholesterol, nf_sodium, nf_total_carbohydrates, nf_dietary_fiber, nf_sugars, nf_proteins, nf_potassium, photo, meal_type):
        self.food_name = food_name
        self.brand_name = brand_name
        self.serving_qty = serving_qty
        self.serving_unit = serving_unit
        self.serving_weight_grams = serving_weight_grams
        self.nf_calories = nf_calories
        self.nf_total_fat = nf_total_fat
        self.nf_saturated_fat = nf_saturated_fat
        self.nf_cholesterol = nf_cholesterol
        self.nf_sodium = nf_sodium
        self.nf_total_carbohydrates = nf_total_carbohydrates
        self.nf_dietary_fiber = nf_dietary_fiber
        self.nf_sugars = nf_sugars
        self.nf_proteins = nf_proteins
        self.nf_potassium = nf_potassium
        self.photo = photo
        self.meal_type = meal_type

class Total:

    def __init__(self, nf_total_fat, nf_saturated_fat, nf_cholesterol, nf_sodium, nf_total_carbohydrates, nf_dietary_fiber, nf_sugars, nf_proteins, nf_potassium):
        self.nf_total_fat = nf_total_fat
        self.nf_saturated_fat = nf_saturated_fat
        self.nf_cholesterol = nf_cholesterol
        self.nf_sodium = nf_sodium
        self.nf_total_carbohydrates = nf_total_carbohydrates
        self.nf_dietary_fiber = nf_dietary_fiber
        self.nf_sugars = nf_sugars
        self.nf_proteins = nf_proteins
        self.nf_potassium = nf_potassium

        
    
