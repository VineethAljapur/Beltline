#from app.routes import mysql
from flask_table import *
from flask import url_for

class EventTable(Table):
    EventName = Col('Event Name')
    SiteName = Col('Site Name')
    price = Col('Ticket Price')
    #tixRemaining = Col('Tickets Remaining')
    #totalVisits = Col('Total Visits')
    #myVisits = Col('My Visits')
    allow_sort = True

    def sort_url(self, col_key, reverse=False):
        if reverse:
            direction = 'desc'
        else:
            direction = 'asc'
        return url_for('exploreEvent', sort=col_key, direction=direction)

class Event(object):
    def __init__(self, EventName, SiteName, price):
        self.EventName = EventName
        self.SiteName = SiteName
        self.price = price


#class Item(object):
    #def __init__(self, name, description):
        #self.name = name
        #self.description = description

#items = [Item('Name1', 'Description1'),
         #Item('Name2', 'Description2'),
         #Item('Name3', 'Description3')]