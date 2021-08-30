from new_backend import db
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from datetime import datetime

class Group(db.Model):
    __tablename__ = 'groups'

    id = db.Column(db.Integer(), primary_key = True)
    internal_id = db.Column(db.String(), unique = True, nullable = False)
    name = db.Column(db.String())
    categories = relationship("Category", backref = "group")

    def __init__(self, name, internal_id):
        self.name = name
        self.internal_id = internal_id

    def __repr__(self):
        return '<id {}>'.format(self.id)