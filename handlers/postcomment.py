from google.appengine.ext import db
from handlers.bloghandle import BlogHandler
from models.comment import comment
from models.post import Post
from main import *
from decorator import *


class PostComment(BlogHandler):
    """Handler for PostComment"""
    @post_exists
    def get(self, post_id, post):
        if user_logged_in(self):
            self.render('postcomment.html', p=post, comment="")
        else:
            self.redirect('/login')

    @post_exists
    def post(self, post_id, post):
        if user_logged_in(self):
            username = self.user.name
            content = self.request.get('content')
            if content:
                c = comment(comment_id=int(post_id), content=content,
                            author=self.user.key())
                c.put()
            time.sleep(0.1)
            self.redirect("/blog")
        else:
            self.redirect('/login')
