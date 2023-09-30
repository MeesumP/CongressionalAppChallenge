from flask import Blueprint, render_template, request
from models import User
from connection import test_shelters

views = Blueprint(__name__, 'views')

@views.route('/')
def home_page():
    return render_template('home.html') #can pass variables to template that render with proper way to call in html code

@views.route('/signup', methods=['GET', 'POST'])
def signup_page():
    biological_sex = request.form.get('sex')
    has_children = request.form.get('children')
    has_disability = request.form.get('disability')
    if has_children == 'YES':
        has_children = True
    else:
        has_children = False

    if mental_disability == 'YES':
        mental_disability = True
    else:
        mental_disability = False

    if has_disability == 'YES':
        has_disability = True
    else:
        has_disability = False

    user = User(biological_sex=biological_sex, has_children=has_children, has_disability=has_disability)
    #data ex: ([('sex', 'male'), ('children', 'NO'), ('mental', 'NO'), ('physical', 'NO')])
    return render_template('signup.html')

@views.route('/results')
def results_page():
    return render_template('results.html', shelters=test_shelters)