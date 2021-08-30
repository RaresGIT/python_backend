from sqlalchemy.orm.relationships import foreign
from new_backend import db
from sqlalchemy import ForeignKey
from datetime import datetime

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer(), primary_key = True)
    internal_id = db.Column(db.String(), unique = True, nullable = False)
    group_id = db.Column(db.String(), ForeignKey('groups.internal_id'))
    color = db.Column(db.String())
    created = db.Column(db.DateTime())
    updated = db.Column(db.DateTime())
    description = db.Column(db.String())
    iconUrl = db.Column(db.String())
    name = db.Column(db.String())
    order = db.Column(db.Integer())
    speechChallenges = db.relationship("Challenge", backref= 'category')
    parent_id = db.Column(db.String())

    def __init__(self, color, description, icon_url, internal_id, name, order, parent_id):
        self.name = name
        self.color = color
        self.description = description
        self.internal_id = internal_id
        self.order = order
        self.iconUrl = icon_url
        self.created = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        self.updated = self.created
        self.parent_id = parent_id

    def __repr__(self):
        return '<id {}>'.format(self.id)