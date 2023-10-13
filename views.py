from flask import Blueprint, render_template, request, redirect, flash
from models import User, db, Ticket
from connection import connection_algorithm

from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, StringField, TextAreaField, PasswordField
from wtforms.validators import InputRequired

views = Blueprint(__name__, 'views')

global admins

admins = [
        {
            "Username": "MAP",
            "Password": "adminpassword123"
        },
        {
           "Username": "CSP",
            "Password": "anotheradminpassword123"
        }
    ]

@views.route('/')
def home_page():
    return render_template('index.html')

@views.route('/signup', methods=['GET', 'POST'])
def signup_page():
    class SignUpForm(FlaskForm):
        biological_sex = RadioField(u'Biological Sex:', choices=['Male', 'Female'], validators=[InputRequired(message="Please input your biological sex")], render_kw={'class': 'list_items'})
        has_children = RadioField(u'Will you bring children with you?', choices=['Yes', 'No'], validators=[InputRequired(message="Please input your whether or not you will bring children")], render_kw={'class': 'list_items'})
        has_disability = RadioField(u'Do you have a physical or mental disability?', choices=['Yes', 'No'], validators=[InputRequired(message="Please input whether or not you have a disability")], render_kw={'class': 'list_items'})
        submit = SubmitField("Submit", render_kw={'class': 'submit_button'})

    form = SignUpForm()

    if form.is_submitted():
        result = request.form
        biological_sex = result.get('biological_sex')
        has_children = result.get('has_children')
        has_disability = result.get('has_disability')

        if has_children == 'Yes':
            has_children = True 
        elif has_children == 'No':
            has_children = False

        if has_disability == 'Yes':
            has_disability = True
        elif has_disability == 'No':
            has_disability = False

        user = User(biological_sex=biological_sex, has_children=has_children, has_disability=has_disability)
        db.session.add(user)
        db.session.commit()

        return redirect('/results')

    return render_template('signup.html', form=form)

@views.route('/results', methods=['GET', 'POST'])
def results_page():
    mostRecentUser = User.query.order_by(User.id.desc()).first()
    possible_shelters = connection_algorithm(mostRecentUser)
    print(f"biological sex: {mostRecentUser.biological_sex}, has children: {mostRecentUser.has_children}, has disability: {mostRecentUser.has_disability}")
    return render_template('results.html', shelters=possible_shelters)

@views.route('/contact', methods=['POST', 'GET'])
def contact_page():
    class ContactForm(FlaskForm):
        email = StringField(u'Email:', render_kw={'class':"textbox-format"})
        info = TextAreaField(u'Please write your question below:', render_kw={'class':"textbox-format"})
        submit = SubmitField("Submit", render_kw={'class': 'submit_button'})

    form = ContactForm()

    if form.is_submitted():
        result = request.form

        email = result.get('email')
        info = result.get('info')

        ticket = Ticket(email=email, info=info)
        db.session.add(ticket)
        db.session.commit()

        return redirect('/thank-you')

    return render_template('contact.html', form=form)

@views.route('/all-shelters')
def allShelters_page():
    shelters = []
    return render_template('all_shelters.html', shelters=shelters)

@views.route('/thank-you')
def thank_youpage():
    return render_template('aftercontactthank.html')

@views.route('/admin', methods=['GET', 'POST'])
def admin_pass_page():
    class LogInForm(FlaskForm):
        username = StringField(u'Username:', render_kw={'class':"textbox-format"})
        password = PasswordField(u'Password:', render_kw={'class':"textbox-format"})
        submit = SubmitField("Submit", render_kw={'class': 'submit_button'})
    form = LogInForm()

    if form.is_submitted():
        result = request.form

        username = result.get('username')
        password = result.get('password')

        for admin in admins:
            if admin["Username"] == username and admin["Password"] == password:
                return redirect('/admin-jksgiosjio&*(jksnbvgkohishg)')
            else:
                return redirect('/')
                #flash('Incorrect username or password', category="error")
    return render_template('admin-pass.html', form=form)

@views.route('/admin-jksgiosjio&*(jksnbvgkohishg)', methods=['GET', 'POST'])
def admin_page():
    contact_tickets = Ticket.query.all()
    return render_template('admin.html', tickets=contact_tickets)