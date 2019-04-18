from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired
#from flask_mysqldb import MySQL

#class flask_mysqldb.MySQL(app=None):
    

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegisterNavigation(FlaskForm):
    userOnly = SubmitField('User Only')
    visitorOnly = SubmitField('Visitor Only')
    employeeOnly = SubmitField('Employee Only')
    employeeVisitor = SubmitField('Employee-Visitor')
    back = SubmitField('Back')

class VisitorForm(FlaskForm):
    fname = StringField('First Name')
    lname = StringField('Last Name')
    username = StringField('Username')
    password = PasswordField('Password')
    conPassword = PasswordField('Confirm Password')
    email = StringField('Email')
    register = SubmitField('Register')
    back = SubmitField('Back')

STATE_ABBREV = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 
                'HI', 'ID', 'IL', 'IN', 'IO', 'KS', 'KY', 'LA', 'ME', 'MD', 
                'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 
                'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 
                'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

class StaffForm(FlaskForm):
    fname = StringField('First Name')
    lname = StringField('Last Name')
    username = StringField('Username')
    userType = SelectField('User Type', choices=['Manager', 'Staff'])
    password = PasswordField('Password')
    conPassword = PasswordField('Confirm Password')
    phone = StringField('Phone')
    address = StringField('Address')
    city = StringField('City')
    state = SelectField('State', choices=STATE_ABBREV)
    zipcode = StringField('Zipcode')
    email = StringField('Email')
    register = SubmitField('Register')
    back = SubmitField('Back')