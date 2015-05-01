from flask import Blueprint, request, jsonify, current_app

emails = Blueprint('emails', __name__)

@emails.route("/")
def index():
	return jsonify({"hello":"emails"})