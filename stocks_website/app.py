from flask import Flask

from stocks_website import routes

app = Flask(__name__)

app.register_blueprint(routes.main_routes)

