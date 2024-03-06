from app import app


@app.route('/')
def hello():
    return '<h1>Form test</h1>'

@app.route('/add/<num1>/<num2>')
def add(num1, num2):
    return f'<h1> {num1} + {num2} = {int(num1) + int(num2)}</h1>'

@app.route('/subtract/<num1>/<num2>')
def subract(num1, num2):
    return f'<h1> {num1} - {num2} = {int(num1) - int(num2)}</h1>'

@app.route('/multiply/<num1>/<num2>')
def multiply(num1, num2):
    return f'<h1> {num1} * {num2} = {int(num1) * int(num2)}</h1>'

@app.route('/division/<num1>/<num2>')
def division(num1, num2):
    return f'<h1> {num1} / {num2} = {int(num1) // int(num2)}</h1>'