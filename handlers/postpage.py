from google.appengine.ext import db
from main import *
from handlers.bloghandle import BlogHandler
from models.post import Post
from decorator import *


class PostPage(BlogHandler):
    """Handler after Posting Posts """
    @post_exists
    def get(self, post_id, post):
        self.render("permalink.html", post=post)
