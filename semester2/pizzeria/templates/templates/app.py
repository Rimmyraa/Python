from flask import Flask, request, send_file, url_for, redirect, abort, render_template



app = Flask(__name__, template_folder='templates', static_folder='static')

dishes = [
    {'dish': 'pizza', 'price': 80},
    {'dish': 'borsh', 'price': 100},
    {'dish': 'burger', 'price': 90},
    {'dish': 'boloneza', 'price': 60},
]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def results():
    context = {
        'title': 'menu',
        'dishes': dishes
    }
    return render_template(template_name_or_list='menu.html', **context)

# def menu_page():
#     return render_template('menu.html')



app.run(host='0.0.0.0', debug=True)