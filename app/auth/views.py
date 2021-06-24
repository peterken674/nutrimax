from flask import render_template,url_for,redirect,flash,request
from . import auth
from ..models import User
from .forms import RegForm,LoginForm
from flask_login import login_user,login_required,logout_user
from ..email import mail_message
from .. import db
import datetime as dt


@auth.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
         user = User.query.filter_by(username = form.username.data).first()
         if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        
        
         flash('Invalid username or Password')
         
    return render_template('auth/login.html', loginform = form)


@auth.route('/signup', methods = ["GET","POST"])
def signup():
    form = RegForm()
    if form.validate_on_submit():
       user = User(email = form.email.data, username = form.username.data, password = form.password.data)
       db.session.add(user)
       db.session.commit()

<<<<<<< HEAD
       mail_message("Welcome to Nutrimax for the best diet","email/welcome_user", user.email,user=user)
       
=======
       mail_message("Welcome to Nutrimax for the best diet","email/welcome_user",
                    user.email,user=user)
       return redirect(url_for("auth.login"))
>>>>>>> 28c95a91de28266bd1d9f5a054803f4da5a3a9f6
       
    title = "New Account | NTMX"       
    return render_template('auth/signup.html',registration_form =form, form=form)
        
        
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been successfully logged out')
    return redirect(url_for("main.index"))
        