from google.appengine.ext import db
from models.comment import comment
from main import *


# post decorator
def post_exists(function):
    def wrapper(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)
        if post:
            return function(self, post_id, post)
        else:
            self.error(404)
            return
    return wrapper


# comment decorator
def comment_exist(function):
    def wrapper(self, comment_id):
        commentobj = comment.get_by_id(int(comment_id))
        if commentobj:
            return function(self, comment_id, commentobj)
        else:
            self.error(404)
            return
    return wrapper


def comment_exists(function):
    def wrapper(self, post_id, comment_id):
        commentobj = comment.get_by_id(int(comment_id))
        if commentobj:
            return function(self, post_id, comment_id, commentobj)
        else:
            self.error(404)
            return
    return wrapper
