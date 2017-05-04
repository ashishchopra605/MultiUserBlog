
from google.appengine.ext import db
from handlers.bloghandle import BlogHandler
from models.comment import comment
from models.post import Post


class BlogFront(BlogHandler):
    """Handler for FrontPage"""
    def get(self):
        posts = Post.all().order('-created')
        comments = comment.all().order('-created')
        self.render('front.html', posts=posts, comment=comments)
