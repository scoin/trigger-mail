from flask import Blueprint, request, jsonify, current_app

users = Blueprint('users', __name__)

@users.route("/")
def index():
	return jsonify({"hello":"greg"})
