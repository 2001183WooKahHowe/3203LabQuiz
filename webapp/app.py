from flask import Flask, render_template, redirect, url_for, request
from flask_jwt_extended import (
    JWTManager, jwt_required, get_jwt_identity, create_access_token, create_refresh_token, jwt_refresh_token_required, get_raw_jwt
    )    
    
#from wtforms import StringField, PasswordField, SubmitField
app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'super-secret'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

jwt= JWTManager(app)
blacklist = set()


@app.route('/')
def login():
    error = None
    if request.method == 'POST':
        if request.form['password'] != 'qweqweqwe':
            error = "invalid creds"
        else:
            return redirect(url_for('home'))        
    return render_template('login.html', error=error)


@app.route('/welcome')
def welcome():
    error = None
    if request.method == 'POST':
        if request.form['password'] != 'qweqweqwe':
            error = "invalid creds"
        else:
            return redirect(url_for('home'))        
    return render_template('welcome.html', error=error)

"""

Password at least 8 char
ensur epw not in wordlist

hash password

"""


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=80)