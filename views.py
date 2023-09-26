from flask import Blueprint, render_template, request

views = Blueprint(__name__, 'views')

@views.route('/')
def home_page():
    return render_template('home.html') #can pass variables to template that render with proper way to call in html code

@views.route('/signup', methods=['GET', 'POST'])
def signup_page():
    biological_sex = request.form.get('sex')
    has_children = request.form.get('children')
    mental_disability = request.form.get('mental')
    physical_disability = request.form.get('physical')
    if has_children.lower() == 'YES':
        has_children = True
    else:
        has_children = False

    if mental_disability.lower() == 'YES':
        mental_disability = True
    else:
        mental_disability = False

    if physical_disability.lower() == 'YES':
        physical_disability = True
    else:
        physical_disability = False

  #  user = User(biological_sex, has_children, mental_disability, physical_disability)
    #data ex: ([('sex', 'male'), ('children', 'NO'), ('mental', 'NO'), ('physical', 'NO')])
    return render_template('signup.html')

@views.route('/results')
def results_page():
    return render_template('results.html')