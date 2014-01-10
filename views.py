from flask import Flask, request, render_template, flash, redirect, url_for
from flask.ext.login import LoginManager, login_user, login_required, UserMixin
from models import *

app = Flask(__name__)
db = SQLAlchemy(app)

login_manager = LoginManager()

app.secret_key = 'developer_key'

login_manager.init_app(app)

newuser = User(name='Paul', email='paul.andy.young@gmail.com', password='whatever')
session = Session()
session.add(newuser)
session.commit()

@login_manager.user_loader
def load_user(userid):
    session = Session()
    return session.query.filter_by(int(userid))

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == 'POST':
        session = Session()
        user = session.query.filter_by(name=request.form['username'])
        if request.form['username'] != user.name:
        #if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != user.password:
        #elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            login_user(user)
            #session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('user_home_page'))
    return render_template('login.html', error=error)

    '''
    form = LoginForm()
    if form.validate_on_submit():
        # login and validate the user...
        login_user(user)
        flash("Logged in successfully.")
        return redirect(request.args.get("next") or url_for("index"))
    return render_template("login.html", form=form)
    '''

@app.route("/", methods=["GET", "POST"])
@login_required
def user_home_page():
    message = "Here is your home page"
    return render_template("user_home_page.html", message=message)


if __name__ == '__main__':
    app.debug = True
    app.run()







'''

username = 'pyoung'
pyoung = {'Name': 'Paul Young', 'Age': 29, 'DOB': '6/27/1984', 'e-mail':'paul.andy.young@gmail.com'}
user_dict = {'pyoung': pyoung}

@app.route("/")
@app.route("/index")
@app.route("/home")
def home_page():
    return 'Home Page!'

@app.route("/1")
def page_one():
    return 'Page One!'

@app.route("/2")
def page_two():
    return 'Page Two!'

@app.route("/user/<username>")
def user_home_page(username):
    line = "Name: " + user_dict[username]['Name'] + " " + "Age: " + str(user_dict[username]['Age'])
    return line
    
if __name__ == '__main__':
    app.debug = True
    app.run()
'''


