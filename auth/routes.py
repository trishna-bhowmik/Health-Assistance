from flask import Blueprint, request, jsonify
from .models import db, User
from flask_jwt_extended import create_access_token
from .utils import hash_password, check_password

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Input validation
    if not username or not password:
        return jsonify({'msg': 'Username and password required'}), 400

    # Check if user already exists
    if User.query.filter_by(username=username).first():
        return jsonify({'msg': 'User already exists'}), 409

    # Create user
    new_user = User(username=username, password=hash_password(password))
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'msg': 'User created successfully'}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'msg': 'Username and password required'}), 400

    user = User.query.filter_by(username=username).first()

    if not user or not check_password(user.password, password):
        return jsonify({'msg': 'Invalid username or password'}), 401

    # Create JWT token
    access_token = create_access_token(identity=user.id)
    return jsonify({'token': access_token}), 200
