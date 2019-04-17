from flask import Flask
from flask import render_template, request, redirect, flash
from flask_mysqldb import MySQL
#from flaskext.mysql import MySQL
from jinja2 import Template
from app import app
from app.forms import LoginForm

#app = Flask(__name__)

mysql = MySQL()
 
# MySQL configurations
'''
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Qwertyuiop44!'
app.config['MYSQL_DATABASE_DB'] = 'beltline'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
'''

#app.config['MYSQL_USER']

@app.route("/" , methods=["GET", "POST"])
def login():
    #if request.form:
        #print(request.form)
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for {}'.format(
            form.email.data))
    return render_template("login_new.html", title="Log In", form=form)

@app.route('/')
def users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM beltline.user''')
    rv = cur.fetchall()
    return str(rv)

@app.route("/register", methods=["POST"])
def register():
    return render_template("register.html")

@app.route("/userOnly", methods=["POST"])
def userOnly():
    return render_template("registerUser.html")

@app.route("/back", methods=["POST"])
def back():
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)