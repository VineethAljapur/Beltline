from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
#from flask_mysqldb import MySQL

#class flask_mysqldb.MySQL(app=None):

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    login = SubmitField('Log In')

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

STATE_ABBREV = [('AL', 'AL'), ('AK', 'AK'), ('AZ', 'AZ'), ('AR', 'AR'), ('CA', 'CA'), ('CO', 'CO'), 
                ('CT', 'CT'), ('DE', 'DE'), ('FL', 'FL'), ('GA', 'GA'), 
                ('HI', 'HI'), ('ID', 'ID'), ('IL', 'IL'), ('IN', 'IN'), ('IO', 'IO'), ('KS', 'KS'),
                ('KY', 'KY'), ('LA', 'LA'), ('ME', 'ME'), ('MD', 'MD'),
                ('MA', 'MA'), ('MI', 'MI'), ('MN', 'MN'), ('MS', 'MS'), ('MO', 'MO'),
                ('MT', 'MT'), ('NE', 'NE'), ('NV', 'NV'), ('NH', 'NH'), ('NJ', 'NJ'), 
                ('NM', 'NM'), ('NY', 'NY'), ('NC', 'NC'), ('ND', 'ND'), ('OH', 'OH'), ('OK', 'OK'), 
                ('OR', 'OR'), ('PA', 'PA'), ('RI', 'RI'), ('SC', 'SC'), 
                ('SD', 'SD'), ('TN', 'TN'), ('TX', 'TX'), ('UT', 'UT'), ('VT', 'VT'), ('VA', 'VA'), 
                ('WA', 'WA'), ('WV', 'WV'), ('WI', 'WI'), ('WY', 'WY')]

employeeType = [('Manager', 'Manager'), ('Staff', 'Staff')]

class StaffForm(FlaskForm):
    fname = StringField('First Name')
    lname = StringField('Last Name')
    username = StringField('Username')
    userType = SelectField('User Type', choices=employeeType)
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

class ExploreEvent(FlaskForm):
    EventName = StringField("Name")
    keyword = StringField("Description Keyword")
    SiteName = SelectField("Site Name", coerce=str)
    StartDate = DateField("Start Date", format='%Y-%M-%D')
    EndDate = DateField("End Date", format='%Y-%M-%D')
    totalVisitsRange = IntegerField("Total Visits Range")
    ticketPriceRange = FloatField("Ticket Price Range")
    includeVisited = BooleanField("Include Visited")
    includeSoldOutEvent = BooleanField("Inclue Sold Out Event")
    #filter = SubmitField("Filter")
    #eventDetail = SubmitField("Event Detail")
    back = SubmitField("Back")
