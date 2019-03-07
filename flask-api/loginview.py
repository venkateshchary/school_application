from app import app, db
from flask import jsonify, request, Response
from models import *
from werkzeug.security import generate_password_hash, \
     check_password_hash


@app.route('/login', methods=['GET'])
def signup():
    print("request:{0} --------request method:{1}".format(request, request.method))
    print(request.json)
    try:
        print("-"*20)
        print(request)
        current_user = Users.query.filter_by(email=request.json['email'],).first()
        print(Users.query.filter_by(email=request.json['email']).first())
        if None == Users.query.filter_by(email=request.json['email']).first():
            if current_user.check_password_hash(request.json["password"]):
                return Response("user is logged in successfully", status=200)
        elif Users.query.filter_by(email=request.json['email']).first():
            return Response("user is already exist", status=409)

    except Exception as e:
        print(e)
        return jsonify({"message":"LOGIN Failed"})