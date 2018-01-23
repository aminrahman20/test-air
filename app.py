import os
from flask import Flask
from flask import request
from pymongo import MongoClient
app = Flask(__name__)
#test

client = MongoClient('mongodb://root:root@ds211558.mlab.com:11558/air_data')
db=client.get_database('air_data')
@app.route('/')
def hello_world():
   return 'Hello World'


@app.route('/val/<co>/<dust>',methods = ['GET'])
def val(co=None,dust=None):
	print(co+" "+dust)	
	db.air_datas.insert_one({'co': co,'dust':dust})
	return co+" "+dust
	
@app.route('/<area>',methods = ['GET'])
def val(area=None):
	print(area)	
	#db.air_datas.insert_one({'co': co,'dust':dust})
	
	return "{'co':'211','du':'211'}"

if __name__ == '__main__':
   app.run(debug=True)
