from app2 import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"