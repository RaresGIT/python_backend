from flask import request, jsonify, Response

from .models.category import Category
from .models.group import Group
from .models.challenge import Challenge
from . import api
from .. import db
from flask_jwt_extended import jwt_required, get_jwt_identity

import json

@api.route('/categories', methods = ['GET'])
def getCategories():

        response = []
        group_id = request.args.get('groupId')
        parent_id = request.args.get('parentId')
        id = request.args.get('id')

        if id:
            categories = Category.query.filter_by(internal_id = id).all()

        if group_id:
            categories = Category.query.filter_by(group_id = group_id).all()

        if parent_id:
            categories = Category.query.filter_by(parent_id = parent_id).all()

        #categories = Category.query.all()
        print(Category.query.all())    
        print(categories)
        for category in categories:

            challenges = []
            target_challenges = Challenge.query.filter_by(category_id = category.internal_id)
            print(target_challenges)

            for challenge in target_challenges:
                challenges.append(challenge.internal_id)

            response.append(
                {
                    'name': category.name,
                    'id': category.internal_id,
                    'color': category.color,
                    'description': category.description,
                    'order': category.order,
                    'iconUrl': category.iconUrl,
                    'created': category.created.__str__(),
                    'updated': category.updated.__str__(),
                    'speechChallenges': challenges,
                    'group_id': category.group_id,
                    'parent_id': category.parent_id
                }
            )
        return Response(json.dumps(response), mimetype='application/json')

@api.route("/create_category", methods = ['POST'])
def createCategory():

        color = request.json.get('color')
        description = request.json.get('description')
        iconUrl = request.json.get('iconUrl')
        internal_id = request.json.get('id')
        name = request.json.get('name')
        order = request.json.get('order')
        group_id = request.json.get('group_id')
        parent_id = request.json.get('parent_id')

        category = Category(color,description,iconUrl,internal_id,name,order,parent_id)

        in_db = Category.query.filter_by(internal_id = internal_id).first()
        if in_db:
            return {'message': 'Category already exists!'}

        target_group = Group.query.filter_by(internal_id = group_id).first()
        target_group.categories.append(category)

        db.session.add(category)
        db.session.commit()

        return {'message': 'Succesfully created category! {name} {description} {group_id}'.format(name = name, description = description, group_id = group_id)}       
