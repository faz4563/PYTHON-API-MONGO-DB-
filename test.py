from flask import Flask
from flask import request
from pymongo import MongoClient
from bson.json_util import dumps
import json
from pymongo import MongoClient
from bson import json_util

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
mydatabase = client["BakeryApplication"]
mycollection = mydatabase["UserDetails"]



@app.route("/get_all_user", methods=['GET'])
def get_all_user():
    try:
        user = mycollection.find()
        # sortedData = mydatabase.aggregate([ "$match"{ country : 'Spain', city : 'Salamanca' }])
        # print(contacts.name)
        return dumps()
    except Exception as e:
        return dumps({'error': str(e)})



        
if (__name__ == "__main__"):
    app.run(debug=True, host='0.0.0.0', port=5003)