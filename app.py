from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/courses')
def courses():
    return render_template("courses.html")

@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

if __name__ == '__main__':
    app.run(debug=True)