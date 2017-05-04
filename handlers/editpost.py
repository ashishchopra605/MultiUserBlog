from google.appengine.ext import db
from handlers.bloghandle import BlogHandler
from models.post import Post
from main import *
from decorator import *


class EditPost(BlogHandler):
    """Handler for EditPost"""
    @post_exists
    def get(self, post_id, post):
        if user_logged_in(self):
            if user_owns_post(self, post):
                self.render("editpost.html", subject=post.subject,
                            content=post.content)
            else:
                error = "you can't edit post"
                self.render("error.html", error=error)
        else:
            self.redirect('/login')

    @post_exists
    def post(self, post_id, post):
        if user_logged_in(self):
            subject = self.request.get('subject')
            content = self.request.get('content')
            if subject and content:
                if user_owns_post(self, post):
                    post.subject = subject
                    post.content = content
                    post.put()
                    self.redirect("/blog/%s" % str(post.key().id()))
                else:
                    error = "you can't edit post"
                    self.render("error.html", error=error)
            else:
                error = "enter subject and content"
                self.render("editpost.html", error=error)
        else:
            self.redirect('/login')
