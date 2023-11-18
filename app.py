
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.j2")

@app.route('/askdog')
def askdog():
    return render_template("ask_dog.j2")

@app.route('/chatdog')
def chatdog():
    return render_template("chat_dog.j2")

if __name__ == '__main__':
    app.run()
