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
    db.air_datas.insert_one({"name":"tamim","id":"201702080"})
    collection = db['air_datas']
    cursor = collection.find({})
    for document in cursor:
        print(document)
        print('\n')
    return 'Hello Tamim!!! How are Boy!!!'

@app.route('/sensor/<name>/<age>',methods = ['POST', 'GET'])
def sensor(name=None,age=None):
   if request.method == 'POST':
      print (request.is_json)
      print("hello\n")
      content = request.json
    #   db.value.insert_one(content)
      print (content)
      
      return "done"
   else:

      return "done " +name+" "+age

if __name__ == '__main__':
   app.run(debug=True)
