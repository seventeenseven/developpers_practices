from flask import Flask, render_template

app = Flask(__name__)


@app.route('/cv/<name>')
def cv_maker(name):
    return render_template(template_name_or_list='cv.html', template_folder='templates/', name=name)

if __name__ == '__main__':
   app.run(debug=True)
"""Your CV should contain:

    Your name
    A picture
    Your hobbies
    Your skills
    Your strengths
    Your weaknesses"""
