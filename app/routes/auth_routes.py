from flask import Blueprint, request, jsonify, session, redirect, url_for
from app.services.auth_service import authenticate_user, register_user

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = authenticate_user(data['email'], data['password'])
    if user:
        session['user_id'] = user.id
        return jsonify({"message": "Login successful"})
    return jsonify({"error": "Invalid credentials"}), 401

@bp.route('/register', methods=['POST'])
def register():
    data = request.json
    register_user(data['email'], data['password'])
    return jsonify({"message": "Registration successful"})
