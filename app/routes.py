from app import app


@app.route('/')
def hello():
    return '<h1>Form test</h1>'