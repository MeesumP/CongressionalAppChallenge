from flask import Blueprint, render_template, request, url_for
from models import Ticket

from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField

admin = Blueprint(__name__, 'admin')

global admins

admins = [
        {
            "Username": "MAP",
            "Password": "adminpassword123"
        },
        {
           "Username": "CSP",
            "Password": "calebisthebestcoderintheworld"
        }
    ]

@admin.route('/', methods=['GET', 'POST'])
def admin_pass_page():
    class LogInForm(FlaskForm):
        username = StringField(u'Username:', render_kw={'class':"textbox-format"})
        password = PasswordField(u'Password:', render_kw={'class':"textbox-format"})
        submit = SubmitField("Submit", render_kw={'class': 'submit_button'})
    
    form = LogInForm()

    loggedIn = False
    contact_tickets = Ticket.query.all()
    failedLogin = False

    if form.is_submitted():
        result = request.form

        username = result.get('username')
        password = result.get('password')

        for admin in admins:
            if admin["Username"] == username and admin["Password"] == password:
                loggedIn = True
                return render_template('admin.html', form=form, loggedIn=loggedIn, tickets=contact_tickets, failedLogin=failedLogin)
            else:
                failedLogin = True
                return render_template('admin.html', form=form, loggedIn=loggedIn, failedLogin=failedLogin)
    return render_template('admin.html', form=form, loggedIn=loggedIn, failedLogin=failedLogin)