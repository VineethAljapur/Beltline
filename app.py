from flask import Flask
from flask import render_template
from flask import request, redirect
from flask_mysqldb import MySQL
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Qwertyuiop44!'
app.config['MYSQL_DATABASE_DB'] = 'beltline'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

#app.config['MYSQL_USER']

@app.route("/") #, methods=["GET", "POST"])
def home():
    #if request.form:
        #print(request.form)
    return render_template("login.html")

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