from google.appengine.ext import db
from models.user import User


class comment(db.Model):
    """Stores Comment Information """
    comment_id = db.IntegerProperty(required=True)
    content = db.StringProperty(required=True)
    author = db.ReferenceProperty(User)
    created = db.DateTimeProperty(auto_now_add=True)
