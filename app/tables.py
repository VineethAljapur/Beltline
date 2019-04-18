#from app.routes import mysql
from flask_table import *

class EventTable(Table):
    name = Col('Name')
    description = Col('Description')
    #EventName = Col('Event Name')
    #SiteName = Col('Site Name')
    #price = Col('Ticket Price')
    #tixRemaining = Col('Tickets Remaining')
    #totalVisits = Col('Total Visits')
    #myVisits = Col('My Visits')

class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

items = [Item('Name1', 'Description1'),
         Item('Name2', 'Description2'),
         Item('Name3', 'Description3')]