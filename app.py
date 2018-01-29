import os
from flask import Flask
from flask.ext.pymongo import PyMongo
from flask import request
#from pymongo import MongoClient
from datetime import datetime
#import datetime
app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'air_data'
app.config['MONGO_URI'] = 'mongodb://root:root@ds211558.mlab.com:11558/air_data'

#test

#print(air_date)
#client = MongoClient('mongodb://root:root@ds211558.mlab.com:11558/air_data')
mongo=PyMongo(app)
@app.route('/add')
def add():
    user = mongo.db.users
    user.insert({'name':'Amin'})
    return 'Added User!'
  
  
if __name__ == '__main__':
   app.run(debug=True)
