from google.appengine.ext import db


class Like(db.Model):
    """Stores Like Information """
    post_id = db.IntegerProperty(required=True)
    user_id = db.IntegerProperty(required=True)
