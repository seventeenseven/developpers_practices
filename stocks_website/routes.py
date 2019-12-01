from flask import Blueprint, render_template

main_routes = Blueprint('main', __name__, 'template/')

@main_routes.route('/')
def index():
    return render_template('index.html', name='Jane')