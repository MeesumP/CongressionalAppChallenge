from flask import Blueprint, render_template

views = Blueprint(__name__, 'views')

@views.route('/')
def home():
    return render_template('home.html') #can pass variables to template that render with proper way to call in html code