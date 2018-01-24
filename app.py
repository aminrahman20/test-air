import os
from flask import Flask
from flask import request
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

#test

#print(air_date)
client = MongoClient('mongodb://root:root@ds211558.mlab.com:11558/air_data')
db=client.get_database('air_data')
@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/val/<co>/<dust>',methods = ['GET'])
def val(co=None,dust=None):
   id = 1
   id += id
   time_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
   print(id+" "+time_date+" "+co+" "+dust)	
   db.air_datas.insert_one({'id':id,'time_date':time_date,'co': co,'dust':dust})
   return id+" "+time_date+" "+co+" "+dust

if __name__ == '__main__':
   app.run(debug=True)
