from flask import Flask, request, send_file, url_for, redirect, abort, render_template
app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu_page():
    return render_template('menu.html')



app.run(host='0.0.0.0', debug=True)