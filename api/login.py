from flask import request, jsonify

from .models.user import User
from .models.group import Group
from . import api
from .. import db
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token


@api.route("/register", methods=["POST"])
def handleRegister():

    username = request.json.get("username")
    password = request.json.get("password")
    school_code = request.json.get("school_code")
    group_id = request.json.get("group_id")
    firstName = request.json.get("firstName")
    lastName = request.json.get("lastName")
    infix = request.json.get("infix")
    metadata = request.json.get("metadata")
    orgId = request.json.get("orgId")

    # add here to db
    user = User(
        username, password, school_code, firstName, lastName, infix, metadata, orgId
    )

    # check if credentials already exist
    user_in_db = User.query.filter_by(
        username=username, password=password, school_code=school_code
    ).first()
    if user_in_db:
        return {"message": "user already registered!"}

    group = Group.query.filter_by(internal_id=group_id).first()

    group.group_association.append(user)
    db.session.add(user)
    db.session.commit()
    return "Succesfully registered user! {username} {password} {school_code}".format(
        username=username, password=password, school_code=school_code
    )


@api.route("/login", methods=["POST"])
def handleLogin():

    username = request.json.get("username")
    password = request.json.get("password")
    school_code = request.json.get("school_code")
    print(username, password, school_code)

    found_user = User.query.filter_by(username=username, password=password).first()
    if found_user:
        access_token = create_access_token(identity={"username": username})
        response = jsonify({"access_token": access_token, "isAuth": "true"})
        return response
    else:
        response = jsonify({"message": "Wrong credentials!", "isAuth": "false"})
        return response


@api.route("/", methods=["GET"])
@jwt_required()
def home():
    current_user = get_jwt_identity()

    return jsonify(logged_in=current_user), 200
