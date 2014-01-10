from flask import Flask, request, render_template, flash, redirect, url_for
from flask.ext.login import LoginManager, login_user, login_required, UserMixin
from database import db_session
from models import *

app = Flask(__name__)
login_manager = LoginManager()
app.secret_key = 'developer_key'
login_manager.init_app(app)


#u1 = User(name='asdf', email='asdf', password='asdf')
#db_session.add(u1)
#db_session.commit()

user1 = db_session.query(User).filter_by(name='asdf').first()
print "User Name: ", user1.name, "User Email: ", user1.email


@login_manager.user_loader
def load_user(id):
    return db_session.query(User).get(int(id))


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == 'POST':
        user = db_session.query(User).filter_by(name=request.form['username']).first()
        if request.form['username'] != user.name:
        #if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != user.password:
        #elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            login_user(user)
            flash('You were logged in')
            return redirect(url_for('user_home_page'))
    return render_template('login.html', error=error)


@app.route("/", methods=["GET", "POST"])
@login_required
def user_home_page():
    message = "Here is your home page"
    return render_template("user_home_page.html", message=message)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


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


