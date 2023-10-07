from flask import Blueprint, render_template, request
from models import User, db
from connection import connection_algorithm, shelters_data

views = Blueprint(__name__, 'views')

@views.route('/')
def home_page():
    return render_template('index.html') #can pass variables to template that render with proper way to call in html code

@views.route('/signup', methods=['GET', 'POST'])
def signup_page():
    if request.method == 'POST':
        biological_sex = request.form.get('male')
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
        print("IS IT WORKING")

        user = User(biological_sex=biological_sex, has_children=has_children, has_disability=has_disability)
        db.session.add(user)
        db.session.commit()
    return render_template('signup.html')

@views.route('/results', methods=['GET', 'POST'])
def results_page():
    #db.session.add(User(biological_sex="Female", has_children=True, has_disability=True))
    #db.session.commit()
    possible_shelters = connection_algorithm(User.query.order_by(User.id.desc()).first())
    print(f"Possible shelters: {possible_shelters}")
    print(f"Users: {User.query.all()}")
    return render_template('results.html', shelters=possible_shelters)