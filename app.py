
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.j2")

if __name__ == '__main__':
    app.run()
