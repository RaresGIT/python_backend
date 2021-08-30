from new_backend import db
from sqlalchemy.orm import relationship

association_table = db.Table(
    "association",
    db.metadata,
    db.Column("user_id", db.String, db.ForeignKey("users.username")),
    db.Column("group_id", db.String, db.ForeignKey("groups.internal_id")),
)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    # hash it later
    password = db.Column(db.String())
    school_code = db.Column(db.String())

    firstName = db.Column(db.String())
    lastName = db.Column(db.String())
    infix = db.Column(db.String())
    metadataString = db.Column(db.String())
    orgId = db.Column(db.String())

    groups = relationship(
        "Group",
        secondary=association_table,
        backref=db.backref("group_association", lazy="dynamic"),
    )

    def __init__(
        self,
        username,
        password,
        school_code,
        firstName,
        lastName,
        infix,
        metadataString,
        orgId,
    ):
        self.username = username
        self.password = password
        self.school_code = school_code
        self.firstName = firstName
        self.lastName = lastName
        self.infix = infix
        self.metadataString = metadataString
        self.orgId = orgId

    def __repr__(self):
        return "<id {}>".format(self.id)
