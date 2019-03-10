from app import app, db
from flask import jsonify, request, Response
from models import *
import re
from flask_cors import CORS, cross_origin
from signup import *

def isValidEmail(email):
    if len(email) > 7:
        if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) != None:
            return True
        return False

@app.route("/home")
def intro():
    return '<p>intro</p>'


@app.route('/')
def home():
    return '<h2> WEL-COME</h2>'

