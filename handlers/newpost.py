from handlers.bloghandle import BlogHandler
from models.post import Post
from models.user import User
from main import *


class NewPost(BlogHandler):
    """Handler for NewPost"""
    def get(self):
        if user_logged_in(self):
            self.render("newpost.html")
        else:
            self.redirect("/login")

    def post(self):
        if not user_logged_in(self):
            self.redirect('/login')
            return

        subject = self.request.get('subject')
        content = self.request.get('content')

        if subject and content:
            p = Post(parent=blog_key(), subject=subject,
                     content=content, user_posted=self.user.key())
            p.put()
            self.redirect('/blog/%s' % str(p.key().id()))
        else:
            error = "subject and content, please!"
            self.render("newpost.html", subject=subject,
                        content=content, error=error)
