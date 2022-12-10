# schema definition
# import from the current package
# same as from website import db
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# one to many situation (one guy having multiple notes)
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # foreign key referencing the specific id
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    # primary key for identification
    id = db.Column(db.Integer, primary_key=True)
    # email should be unique, no duplicate accounts for same email
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    nickname = db.Column(db.String(150))
    notes = db.relationship('Note')