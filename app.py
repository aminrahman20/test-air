import os
from flask import Flask
from flask.ext.pymongo import pymongo
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
db=PyMongo(app)
@app.route('/home')
def hello_world():
   return 'Hello World'
  
  
if __name__ == '__main__':
   app.run(debug=True)
