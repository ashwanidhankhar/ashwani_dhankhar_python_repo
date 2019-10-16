# HTML inside Python Flask

from flask import Flask
app = Flask(__name__)

@app.route('/Lavish')
def index():
    return '<html><body><h1>Welcome to BSDU</h1></body></html>'

if __name__ == '__main__':
    app.run()