from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create_tour/')
def create_tour():
    return render_template('create_tour.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
