from flask import Flask
from flask import render_template, request, redirect, flash, make_response, Markup, url_for
from flask_login import login_user, current_user, logout_user, login_required
#from flask_mysqldb import MySQL
import hashlib
from pymysql import IntegrityError
#import mysql
#from flaskext.mysql import MySQL
from jinja2 import Template
from app import app
from app.forms import *
from app.tables import *
from collections import OrderedDict
import mysql.connector
 
# MySQL configurations
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'Qwertyuiop44!'
#app.config['MYSQL_DB'] = 'beltline'
#app.config['MYSQL_HOST'] = 'localhost'
#app.config['DEBUG'] = 'True'

#mysql = MySQL(app)
conn = mysql.connector.connect(host='localhost',
                            database='beltline',
                            user='root',
                            password='Qwertyuiop44!')


# Log In (Main) Page
@app.route("/")
@app.route("/login" , methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.login.data and form.validate_on_submit:
        #redirect('/visitorFunc')
        return render_template("visitorFunc.html")
    #if form.validate_on_submit():
        #flash('Login requested for {}'.format(
            #form.email.data))
    return render_template("login_new.html", title="Log In", form=form)

@app.route("/registerNavigation", methods=["GET", "POST"])
def registerNavigation():
    form = RegisterNavigation()
    if form.validate_on_submit():
        if form.userOnly.data:
            return redirect('/registerVisitor')
        elif form.visitorOnly.data:
            return redirect('/registerVisitor')
        elif form.employeeOnly.data:
            return redirect('/registerStaff')
        elif form.employeeVisitor.data:
            return redirect('/registerStaff')
        elif form.back.data:
            return redirect('/')
    return render_template("registerNavigation.html", form=form)

@app.route("/registerVisitor", methods=["GET", "POST"])
def registerVisitor():
    form = VisitorForm()
    if form.validate_on_submit() and form.register.data:
        fname = form.fname.data
        lname = form.lname.data
        username = form.username.data.lower()
        password = form.password.data
        password = hashlib.sha1(password.encode()).hexdigest()
        email = form.email.data.lower()
        #conn = mysql.connect()
        cur = conn.cursor()
        cur.execute('SELECT * FROM user WHERE username = "%s" ' % username)
        rv = cur.fetchone()
        if rv is None:
            cur.execute('SELECT * FROM email WHERE email_address = "%s" AND username = "%s"' % (email, username))
            rv = cur.fetchone()
            if rv is None:
                cur.execute('INSERT INTO user (firstname, lastname, username, password, status) VALUES (%s, %s, %s, %s, %s)',
                            (fname, lname, username, password, 'Pending'))
                cur.execute('INSERT INTO visitor VALUE (%s)', [username])
                conn.commit()
                flash('Sign up successful! (Approval Pending)')
                return redirect(url_for('login'))
            else:
                flash('This email already exists!')
        else:
            flash('Username already exists!')
        if form.back.data and form.validate_on_submit():
            return redirect('/registerNavigation')
    return render_template("registerVisitor.html", form=form)

@app.route("/visitorFunc", methods=["POST"])
def visitorFunc():
    return render_template('visitorFunc.html')

@app.route("/exploreEvent", methods=["GET", "POST"])
def exploreEvent():
    cur = conn.cursor()
    cur.execute('SELECT SiteName FROM site')
    #rv = cur.fetchall()
    form = ExploreEvent()
    #form.SiteName.choices = rv
    form.SiteName.choices = [(g[0], g[0]) for g in cur.fetchall()]#rv['label']]
    table = EventTable(items)
    return render_template("exploreEvent.html", form=form, table=table)

@app.route("/back", methods=["POST"])
def back():
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)