from flask import Blueprint, request, jsonify, current_app

main = Blueprint('main', __name__)

@main.route("/")
def index():
	return jsonify({"hello":"greg"})
