from google.appengine.ext import db
from handlers.bloghandle import BlogHandler
from models.post import Post
from main import *


class UserPage(BlogHandler):
    """Handler for UserPage"""
    def get(self):
        if user_logged_in(self):
            username = self.user.name
            posts = Post.all().filter('user_posted =', self.user.key())
            self.render('userpage.html', username=username, posts=posts)
        else:
            self.redirect('/login')
