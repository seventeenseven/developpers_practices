import datetime
from flask import Flask, render_template_string


app = Flask(__name__)

@app.route('/greet/<name>')
def greetin(name):
    hour_ = datetime.datetime.now().hour
    template = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Greeting you</title>
    </head>
    <body>
        {%if hour in (8,9,10,11,12) %}
            <h1>Good Morning {{name}}, Have a good day</h1>
        {% elif hour in (13,14,15,16) %}
            <h1>Good Afternoon {{name}}, Hope you having a good day</h1>
        {% elif hour in (17,18,19,20) %}
            <h1>Good Evening {{name}}</h1>
        {% else %}
            <h1>Good Nigth {{name}}</h1>
        {% endif %}
    </body>
    </html>
    '''
    return render_template_string(template, hour = hour_, name=name)

app.run()