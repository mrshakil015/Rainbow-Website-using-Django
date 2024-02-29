from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

AUTHORIZED_PASSWORD = "shakil015"
AUTHORIZED_USER= "shakil015"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/courses')
def courses():
    return render_template("courses.html")

@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

@app.route('/admin', methods=['POST', 'GET'])
def admin_login():
    if request.method == 'POST':
        admin_username = request.form['admin_username']
        admin_password = request.form['admin_password']
        print(admin_username)
        print(admin_password)

        if (admin_username == AUTHORIZED_USER) and (admin_password == AUTHORIZED_PASSWORD):
            print("It works")
            # session['admin_logged_in'] = True
            return redirect(url_for('index'))
        else:
            error_message = "Invalid admin credentials"
            return render_template('adminlogin.html', error_message=error_message)
    else:
        return render_template('adminlogin.html', error_message=None)

if __name__ == '__main__':
    app.run(debug=True, port=8000)