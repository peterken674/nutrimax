from flask_mail import Message
from flask import render_template
from . import mail

def mail_message(subject,template,to,**kwargs):
<<<<<<< HEAD
    sender_email = 'peter.kimani@student.moringaschool.com'
=======
    sender_email = 'robertokello443@gmail.com'
>>>>>>> 28c95a91de28266bd1d9f5a054803f4da5a3a9f6
    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)

def mail_feedback(subject,template,to):
    sender_email = 'peter.kimani@student.moringaschool.com'
    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= template
    mail.send(email)