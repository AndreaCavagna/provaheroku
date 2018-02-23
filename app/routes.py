from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/bra')
def index():
    return "Hello, Bra!"