from app import app, db
from flask import jsonify, request, Response
from models import *
from werkzeug.security import check_password_hash


@app.route('/login', methods=['POST'])
def login():
    try:
        current_user = Users.query.filter_by(username=request.form["username"],).first()
        if Users.query.filter_by(username=request.form["username"]).first():
            if check_password_hash(current_user.password, request.form["password"]):
                return Response("user is logged in successfully", status=200)
        else:
            return Response("user is does not exist", status=409)
    except TypeError as e:
        return jsonify({"Error@login": ":%s" % e})
