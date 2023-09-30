from flask import Blueprint, render_template, request
from models import User, db
from connection import find_user, connection_algorithm, test_shelters

views = Blueprint(__name__, 'views')

@views.route('/')
def home_page():
    return render_template('index.html') #can pass variables to template that render with proper way to call in html code

@views.route('/signup', methods=['GET', 'POST'])
def signup_page():
    biological_sex = request.form.get('sex')
    has_children = request.form.get('children')
    has_disability = request.form.get('disability')
    if has_children == 'YES':
        has_children = True
    else:
        has_children = False

    if has_disability == 'YES':
        has_disability = True
    else:
        has_disability = False

    user = User(biological_sex=biological_sex, has_children=has_children, has_disability=has_disability)
    db.session.add(user)
    db.session.commit()
    return render_template('signup.html')

@views.route('/results', methods=['GET', 'POST'])
def results_page():
    return render_template('results.html', shelters=test_shelters)