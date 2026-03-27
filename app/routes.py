from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')



@main.route('/market')
def market():
    return render_template('market.html')

@main.route('/about')
def about():
    return render_template('about.html')