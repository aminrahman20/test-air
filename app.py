import os
from flask import Flask
from flask import request
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime
#import datetime
app = Flask(__name__)
CORS(app)
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
    results = db.air_datas.find().sort("time_date",-1)
    #for record in results:
        #print(record['co'])
    
    return results[0]['co']
    
   
#@app.route('/val/<co>/<dust>',methods = ['GET'])
#def val(co=None,dust=None):
   
    #time_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #print(time_date+" "+co+" "+dust)	
    #db.air_datas.insert_one({'time_date':time_date,'co': co,'dust':dust})
  
    #return time_date+" "+co+" "+dust
@app.route('/val/<co>',methods = ['GET'])
def val(co=None):
    time_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S +0000', gmtime())
    print(time_date+" "+co)	
    db.air_datas.insert_one({'time_date':time_date,'co': co})
    return time_date+" "+co

if __name__ == '__main__':
    app.run(debug=True)
