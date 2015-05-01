from flask import Blueprint, request, jsonify, current_app

campaigns = Blueprint('campaigns', __name__)

@campaigns.route("/")
def index():
	return jsonify({"hello":"campaigns"})