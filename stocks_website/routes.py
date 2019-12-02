from flask import Blueprint, render_template

main_routes = Blueprint('main', __name__, template_folder='template/')


@main_routes.route('/')
def index():
    """@main_routes.route('/home/<username>')
def index(username):"""
    """template = '''
    <html>
        <head>
            <title>Home Page - Microblog</title>
        </head>
        <body>
            <h1>Hello, {{ name }}!</h1>
        </body>
    </html>'''
    html = flask.render_template_string( template, name=username )
    return html"""
    return render_template('index.html', name='Jane')