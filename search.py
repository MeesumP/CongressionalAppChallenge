from flask import Blueprint, render_template, request, redirect, url_for
from models import User, db
from connection import connection_algorithm, shelters_data

from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.validators import InputRequired

search = Blueprint(__name__, 'search')

@search.route('/', methods=['GET', 'POST'])
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

        return redirect('/search/results')

    return render_template('signup.html', form=form)

@search.route('/results', methods=['GET', 'POST'])
def results_page():
    mostRecentUser = User.query.order_by(User.id.desc()).first()
    possible_shelters = connection_algorithm(mostRecentUser)
    return render_template('results.html', shelters=possible_shelters)

@search.route('/all-shelters')
def allShelters_page():
    shelters = shelters_data
    return render_template('results.html', shelters=shelters)