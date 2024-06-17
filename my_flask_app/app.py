from flask import Flask
import os


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

@app.route('/')
def hello_world():
    return 'Moe Flask приложение в контейнере Docker.'
 
if __name__ == '__main__':
    app.run()