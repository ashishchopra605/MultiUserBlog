from google.appengine.ext import db
from handlers.bloghandle import BlogHandler
from models.comment import comment
from main import *
from decorator import *


class EditComment(BlogHandler):
    """Handler for EditComment"""
    @comment_exists
    def get(self, post_id, comment_id, commentobj):
        if user_logged_in(self):
            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            post = db.get(key)
            if post and user_owns_comment(self, commentobj):
                self.render('editcomment.html', p=post, comment=commentobj)
            else:
                error = "You can't edit others comments"
                self.render("error.html", error=error)
        else:
            self.redirect('/login')

    @comment_exists
    def post(self, post_id, comment_id, commentobj):
        if user_logged_in(self):
            content = self.request.get("content")
            if content and user_owns_comment(self, commentobj):
                commentobj.content = content
                commentobj.put()
                time.sleep(0.1)
                self.redirect('/blog')
            else:
                error = "You can't edit others comments"
                self.render("error.html", error=error)
        else:
            self.redirect('/login')
