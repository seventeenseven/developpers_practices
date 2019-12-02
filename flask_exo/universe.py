from flask import Flask, render_template_string, render_template
import json

app = Flask(__name__)


@app.route('/realm/<realm>')
def realm_index(realm):
    with open('templates/realm.jinja', 'r') as f:
        html = f.read()
        return render_template_string(html, realm=realm)


@app.route('/particles')
def particles_view():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return render_template('particles.html', particles=data)

if __name__ == '__main__':
    app.run()