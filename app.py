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
   def val(co=None,dust=None,time_date=None):
   time_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
   print(co+" "+dust+" "+time_date)	
   db.air_datas.insert_one({'co': co,'dust':dust,'time_date':time_date})
   return co+" "+dust+" "+time_date

if __name__ == '__main__':
   app.run(debug=True)
