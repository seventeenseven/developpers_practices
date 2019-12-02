from flask import Flask, render_template
from my_market_place import database_manager

app = Flask(__name__)
database_manager.create_database()
@app.route("/")
def homepage():
    template = "<h1>Welcome to my market place</h1>" \
               "<button><a href=\"products\">Check the products List</a></button>"
    return template


@app.route("/products")
def products_page():

    data = database_manager.load_database()
    css = open('static/style.css', 'r').read()
    return render_template('index.html', products=data, additional_css=css)


@app.route('/products/<product_id>')
def product_detail(product_id):
    data = database_manager.load_database()
    css = open('static/style.css', 'r').read()
    prod = list(filter(lambda  x: x['ProductId']== product_id, data))
    return render_template('details.html', prod=prod[0], additional_css=css)

app.run(debug=True)