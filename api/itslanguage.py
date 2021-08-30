from flask import json, request, jsonify, Response, send_file

from . import api
from .. import db
from flask_jwt_extended import jwt_required, get_jwt_identity


@api.route("/itslanguage/<filename>", methods=["GET"])
def itslanguage(filename):
    path = "api/downloads/logos/{filename}".format(filename=filename)
    return send_file(path)
