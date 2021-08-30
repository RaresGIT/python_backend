from .models.category import Category
from flask import request, jsonify, Response

from .models.group import Group
from .models.user import User
from . import api
from .. import db
from flask_jwt_extended import jwt_required, get_jwt_identity

import json

@api.route("/groups", methods = ['GET'])
@jwt_required()
def handleGroups():

        current_user = get_jwt_identity()
        print(current_user["username"])
        user = User.query.filter_by(username = current_user["username"]).first()
        
        # print(user.groups[0].internal_id)
        groups = []

        for group in user.groups:
            groups.append(group.internal_id)
    
        print(groups)
        response = []
        for group_id in groups:

            target_categories = Category.query.filter_by(group_id = group_id).all()
            print(target_categories)

            categories = []
            for category in target_categories:
                categories.append(category.internal_id)

            response.append(
                {
                    'name': group.name,
                    'categories': categories,
                    "id": group.internal_id
                }
            )
        return Response(json.dumps(response), mimetype='application/json')
        


@api.route("/create_group", methods = ['POST'])
def createGroup():

        name = request.json.get('name')
        internal_id = request.json.get('id')
        group = Group(name,internal_id)
        
        check_in_db = Group.query.filter_by(name = name).first()
        if check_in_db:
            return {'message': "Group already exists!"}

        db.session.add(group)
        db.session.commit()
        return "Succesfully created group! {name}".format(name = name)
