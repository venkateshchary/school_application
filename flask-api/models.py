from app import db
# from werkzeug.security import generate_password_hash
# from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash, \
     check_password_hash
import re