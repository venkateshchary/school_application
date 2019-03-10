from app import app, db
from flask import jsonify, request, Response
from models import *


@app.route('/batch', methods=['GET', 'POST'])
def batch():
    if request.method == "GET":
        try:
            pass
        except ValueError:
            raise
    else:
        try:
            if None == Batch.query.filter_by(year=request.json['year']).first():
                year = Batch(year=request.json["year"])
                db.session.add(year)
                db.session.commit()
                return Response("Batch is created successfully", status=200)
            else:
                return jsonify({"Error": "Batch is already exists"})
        except ValueError:
            return Response("Batch is not added ", status=400)
