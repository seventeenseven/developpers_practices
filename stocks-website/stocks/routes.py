from flask import Blueprint

main_routes = Blueprint('main', __name__, 'templates/')

@main_routes.route('/')
def index():
    return 'Hi'