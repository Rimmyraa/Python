from flask import Flask, render_template, request

app = Flask(__name__)


API_KEY = '1d42a6bb77c83fbbb2ab9deee55c1ffb'

def get_current_weather(city):
    URL = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}'
    response = request.get(URL)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None


@app.route('/')
def index():
    city = 'Київ'
    current_weather = get_current_weather(city)
    return render_template('index.html', current_weather=current_weather, title1="Oderman")

@app.route("/menu/")
def menu():
    return render_template('menu.html', title1="Меню")

@app.route("/add_pizza/", methods=["GET", "POST"])
def add_pizza():
    current_weather = get_current_weather(city="Київ")
    if request.method == "POST":
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        return render_template('index.html', current_weather=current_weather)
    else:
        return render_template('join.html')





if __name__ == '__main__':
    app.run(debug=False)