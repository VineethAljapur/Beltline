from flask import Flask
from app.config import Config
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config.from_object(Config)

from app import routes

from flaskext.mysql import MySQL
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Qwertyuiop44!'
app.config['MYSQL_DATABASE_DB'] = 'beltline'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL(app)

mysql.init_app(app)