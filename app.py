from flask import Flask
import toml

app = Flask(__name__)
app.config.from_file('config.toml', toml.load)

@app.route('/')
def hello_world():
    return '<p>Hello, {greeting}</p>'.format(greeting=app.config['GREETING'])