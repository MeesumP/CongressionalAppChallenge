from flask import Blueprint, render_template, request

views = Blueprint(__name__, 'views')

@views.route('/')
def home_page():
    return render_template('home.html') #can pass variables to template that render with proper way to call in html code

@views.route('/signup', methods=['GET', 'POST'])
def signup_page():
    if request.method == 'POST':
        biological_sex = request.form.get('sex')
    print(biological_sex)
    #data ex: ([('sex', 'male'), ('children', 'NO'), ('mental', 'NO'), ('physical', 'NO')])
    return render_template('signup.html')

@views.route('/results')
def results_page():
    return render_template('results.html')