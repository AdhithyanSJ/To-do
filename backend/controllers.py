from flask_restful import Resource
from flask import request,jsonify
from models import User, db , todo
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash