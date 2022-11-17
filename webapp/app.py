from flask import Flask, render_template, redirect, url_for, request
from wtforms import StringField, PasswordField, SubmitField
app = Flask(__name__)

@app.route('/')
def home():
    return "Flask Dockerized"

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = "invalid creds"
        else:
            return redirect(url_for('home'))        
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')