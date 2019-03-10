from app import app, db
from flask import jsonify, request, Response
from models import *
import re
from flask_cors import CORS, cross_origin

# def isValidEmail(email):
#     if len(email) > 7:
#         if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) != None:
#             return True
#         return False


@app.route('/signup', methods=['POST'])
def signup():
    print("request:{0} --------request method:{1}".format(request, request.method))
    print(request.json)
    try:
        print("-"*20)
        print(request)
        current_user = Users.query.filter_by(email=request.json['email']).first()
        print(Users.query.filter_by(email=request.json['email']).first())
        if None == Users.query.filter_by(email=request.json['email']).first():
            print("user does not exists")
            # if isValidEmail(request.json['email']):
            u = Users(request.json['username'], request.json['password'], request.json['email'],\
                      request.json['renterpassword'])
            db.session.add(u)
            db.session.commit()
            # else:
            #     return Response("invalid email address",status=409)
            return Response("user is created successfully", status=200)
        elif Users.query.filter_by(email=request.json['email']).first():
            return Response("user is already exist",status=409)

    except Exception as e:
        print(e)
        return jsonify({"message":"email is already exists"})