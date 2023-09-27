from flask import Blueprint, render_template

views = Blueprint(__name__, 'views')

@views.route('/')
def home_page():
    return render_template('index.html') #can pass variables to template that render with proper way to call in html code

@views.route('/signup')
def signup_page():
    return render_template('signup.html')

@views.route('/results')
def results_page():
    return render_template('results.html')