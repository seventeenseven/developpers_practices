from flask import Flask
from stocks_website import routes

app = Flask(__name__)

app.register_blueprint(routes.main_routes)

if __name__ == '__main__':
    app.run()