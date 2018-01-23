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


if __name__ == '__main__':
   app.run(debug=True)
