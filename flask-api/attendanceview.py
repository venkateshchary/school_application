from app import app, db
from flask import jsonify, request, Response
from models import *


@app.route('/attendance', methods=['GET', 'POST'])
def attendance():
    print(request)
    if request.method =="GET":
        print("--------------------get request")
        try:
            if "from" in request and "to" in request:
                pass
                # TODO : WRITE A QUERY TO GET THE DATE WISE DATA

            if "date" in request:
                attendance = Classes.query.filter_by(date=request.form["date"])

        except ValueError:
            raise
    else:
        print("--------------------------post:")
        try:
            if None == Attendance.query.filter_by(student_name=request.json['student_name'],
                                               date=request.json["date"],
                                                class_id=request.json["class_id"],
                                                batch_id=request.json["batch_id"]).first():
                att_obj = Attendance.query.filter_by(student_name=request.json['student_name'],
                                               date = request.json["date"],
                                                classid=request.json["class_id"],
                                                batch_id=request.json["batch_id"]).first()
                db.session.add(att_obj)
                db.session.commit()
                return Response("attendance is created successfully", status=200)
            else:
                return jsonify({"Error": "attendance is already exists"})
        except Exception as e:
            print("*"*30)
            raise
