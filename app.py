from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World!<h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f'Hello {name}'


@app.route('/convert_f_to_c')
@app.route('/convert_f_to_c/<fahrenheit>')
def convert_f_to_c_page(fahrenheit=0.0):
    fahrenheit = float(fahrenheit)
    celsius = convert_fahrenheit_to_celsius(fahrenheit)
    return f"{fahrenheit:.2f} F is equal to {celsius:.2f} C"


@app.route('/convert_c_to_f')
@app.route('/convert_c_to_f/<celsius>')
def convert_c_to_f_page(celsius=0.0):
    celsius = float(celsius)
    fahrenheit = convert_celsius_to_fahrenheit(celsius)
    return f"{celsius:.2f} C is equal to {fahrenheit:.2f} F"


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert fahrenheit to celsius"""
    return 5 / 9 * (fahrenheit - 32)


def convert_celsius_to_fahrenheit(celsius):
    """convert celsius to fahrenheit"""
    return celsius * 9 / 5 + 32


if __name__ == '__main__':
    app.run()
