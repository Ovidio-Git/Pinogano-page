from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hellou bro'


if __name__ == '__main__':
    app.run()