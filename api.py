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


def rep(__self__):
    mycollection.__format__


@app.route("/add_user", methods=['POST'])
def add_user():
    try:
        data = json.loads(request.data)
        name = data['name']
        email = data['email']
        password = data['password']
        phone = data["phone"]


        dup_data = mycollection.distinct("phone")
        print(dup_data)
        if (phone not in dup_data):
            status = mycollection.insert_one({
                "name": name,
                "email": email,
                "password": password,
                "phone": phone
            })
            print(status)
            return dumps({'Status': 'User Created Successfully'})
        else:
            return dumps({'Status': 'User Already Exists'})
    except Exception as e:
        return dumps({'error': str(e)})


@app.route("/get_all_user", methods=['GET'])
def get_all_user():
    try:
        user = mycollection.find()
        return dumps(user)
    except Exception as e:
        return dumps({'error': str(e)})


@app.route("/get_user_detail/<name>", methods=['GET'])
def get_user_detail(name):
    try:
        x = mycollection.find_one({"name": name})
        return dumps(x)
    except Exception as e:
        return dumps({'error': str(e)})


@app.route("/update_user_detail/<name>", methods=['PUT'])
def update_user_detail(name):
    try:
        data = json.loads(request.data)
        x = mycollection.find_one({"name": name})
        myquery = {"name": x['name']}
        newvalues = {
            "$set": {
                "name": data["name"],
                "email": data["email"],
                "password": data["password"],
                "phone": data["phone"]
            }
        }
        status = mycollection.update_one(myquery, newvalues)
        print(status)
        return dumps({'message': 'SUCCESS'})
    except Exception as e:
        return dumps({'error': str(e)})


@app.route("/delete_user_detail/<name>", methods=['DELETE'])
def delete_user_detail(name):
    try:
        x = mycollection.find_one({"name": name})
        status = mycollection.delete_one(x)
        return dumps({'message': 'SUCCESS'})
    except Exception as e:
        return dumps({'error': str(e)})


@app.route("/add_admin", methods=['POST'])
def add_admin():
    try:
        data = json.loads(request.data)
        name = data['name']
        email = data['email']
        password = data['password']
        phone = data["phone"]
        admin = data["admin"]
        status = mycollection.insert_one({
            "name": name,
            "email": email,
            "password": password,
            "phone": phone,
            "admin": admin,
        })
        print(status)
        return dumps({
            'Status': 'User Created Successfully',
            'Status_code': 200
        })

    except Exception as e:
        return dumps({'error': str(e)})


@app.route("/add_super_admin", methods=['POST'])
def add_super_admin():
    try:
        data = json.loads(request.data)
        name = data['name']
        email = data['email']
        password = data['password']
        phone = data["phone"]
        super_admin = data["super_admin"]
        status = mycollection.insert_one({
            "name": name,
            "email": email,
            "password": password,
            "phone": phone,
            "admin": super_admin
        })
        print(status)
        return dumps({
            'Status': 'User Created Successfully',
            'Status_code': 200
        })
    except Exception as e:
        return dumps({
            'error': str(e),
        })


# @app.route("/get_all_admin", methods=['GET'])
# def get_all_admin():
#     try:
#         user = mycollection.find()
#         # print(contacts.name)
#         return dumps(user)
#     except Exception as e:
#         return dumps({'error': str(e)})

# @app.route("/get_admin_detail/<admin>", methods=['GET'])
# def get_admin_detail(admin):
#     try:
#         x = mycollection.find_one({"admin": admin})
#         return dumps({
#             "id": x['id'],
#             "name": x['name'],
#             "email": x['email'],
#             "password": x['password'],
#             "phone": x['phone']
#         })
#     except Exception as e:
#         return dumps({'error': str(e)})

# @app.route("/update_admin/<name>", methods=['PUT'])
# def update_admin_detail(name):
#     try:
#         data = json.loads(request.data)
#         x = mycollection.find_one({"name": name})
#         data = {"name": x['name'], "contact": x['contact']}
#         newvalues = {{"name": data["name"], "contact": data["contact"]}}
#         status = mycollection.update_one(data, newvalues)
#         print(status)
#         return dumps({'Status': 'Data Updated', 'Status_code': 200})
#     except Exception as e:
#         return dumps({'error': str(e)})

# @app.route("/delete_admin/<name>", methods=['DELETE'])
# def delete_admin_detail(name):
#     try:
#         x = mycollection.find_one({"name": name})
#         status = mycollection.delete_one(x)
#         return dumps({'Status': 'Deleted Successfully', 'Status_code': 200})
#     except Exception as e:
#         return dumps({'error': str(e)})


@app.route("/")
def home():
    return "Welcome!"


if (__name__ == "__main__"):
   app.run(debug=True, host='127.0.0.1', port=5500)
