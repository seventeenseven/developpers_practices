from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def date_view():
    date = datetime.now()
    html = f"<h1>Today's date:{date}</h1>"
    return html


if __name__ == '__main__':
    app.run()