from app import app, db
from flask import jsonify, request, Response
from models import *


@app.route('/class', methods=['GET', 'POST'])
def classes():
    if request.method =="GET":
        try:
            if "from" in request and "to" in request:
                pass
                # TODO : WRITE A QUERY TO GET THE DATE WISE DATA

            if "date" in request:
                attendance = Classes.query.filter_by(date=request.form["date"])

        except ValueError:
            raise
    else:
        try:
            if None == Classes.query.filter_by(name=request.json['name'], batch_id=request.json["batch_id"]).first():
                clas_obj = Classes(name=request.json["name"], batch_id=request.json["batch_id"])
                db.session.add(clas_obj)
                db.session.commit()
                return Response("Class is created successfully", status=200)
            else:
                return jsonify({"Error": "class is already exists"})
        except ValueError:
            raise