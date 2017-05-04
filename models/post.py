from google.appengine.ext import db
from main import *
from models.user import User


class Post(db.Model):
    """Stores Posts Information """
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    user_posted = db.ReferenceProperty(User)
    _likes = db.IntegerProperty(default=0)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)

    def render(self):
        self._render_text = self.content.replace('\n', '<br>')
        return render_str("post.html", p=self)

    @property
    def likes(self):
        return self._likes

    @likes.setter
    def likes(self, like):
        self._likes = like
