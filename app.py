import os
from flask import Flask
from flask import request
from pymongo import MongoClient
from datetime import datetime
import datetime
app = Flask(__name__)

#test

#print(air_date)
client = MongoClient('mongodb://root:root@ds211558.mlab.com:11558/air_data')
db=client.get_database('air_data')
@app.route('/')
def hello_world():
   return 'Hello World'
@app.route('/time',methods = ['GET'])
def time():
   #x=datetime.datetime.now()
   #y=datetime.datetime.now() - datetime.timedelta(minutes=20)
   #db.air_datas.find({time_date: {$gte:y,$lt: x}})
   
   return "{'co':'123','du':'432'}"
   
@app.route('/val/<co>/<dust>',methods = ['GET'])
def val(co=None,dust=None):
   
   time_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
   print(time_date+" "+co+" "+dust)	
   db.air_datas.insert_one({'time_date':time_date,'co': co,'dust':dust})
   return time_date+" "+co+" "+dust

if __name__ == '__main__':
   app.run(debug=True)
