from app import db
# from werkzeug.security import generate_password_hash
# from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash, \
     check_password_hash
from sqlalchemy import ForeignKey


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    renterpassword = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(120), nullable=False)

    def __init__(self, username, password, email, renterpassword):
        self.username = username
        self.email = email
        self.renterpassword = renterpassword
        self.password = self.set_password(password)

    def set_password(self, password):
        return generate_password_hash(password)

    def check_password(self, passwordcheck):
        return check_password_hash(self.password, passwordcheck)

    def password_check(self, password, renterpassword):
        print(password, renterpassword)
        if password == renterpassword:
            return True


class Batch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)


class Classes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    batch_id = db.Column(db.Integer, ForeignKey('batch.id'))


class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime(), nullable=False)
    class_id = db.Column(db.Integer, ForeignKey('classes.id'))
    batch_id = db.Column(db.Integer, ForeignKey('batch.id'))

# TODO :CREATE A ABSTRACT DB MODEL
