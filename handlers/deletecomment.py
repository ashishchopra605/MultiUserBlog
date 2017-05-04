from google.appengine.ext import db
from handlers.bloghandle import BlogHandler
from decorator import *
from main import *
import time


class DeleteComment(BlogHandler):
    """Handler for DeleteComment"""
    @comment_exist
    def post(self, comment_id, commentobj):
        if user_logged_in(self):
            if user_owns_comment(self, commentobj):
                commentobj.delete()
                time.sleep(0.1)
                self.redirect('/blog')
            else:
                error = "You can't delete others comments"
                self.render("error.html", error=error)
        else:
            self.redirect('/login')
