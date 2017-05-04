from google.appengine.ext import db
from handlers.bloghandle import BlogHandler
from models.comment import comment
from decorator import *
from main import *


class DeletePost(BlogHandler):
    """Handler for DeletePost"""
    @post_exists
    def post(self, post_id, post):
        if user_logged_in(self):
            if post and user_owns_post(self, post):
                post.delete()
                commentobj = comment.all().filter('comment_id =',
                                                  int(post_id)).get()
                if commentobj:
                    commentobj.delete()
                time.sleep(0.1)
                self.redirect('/blog/user')
            else:
                error = "you can't delete post"
                self.render("error.html", error=error)
        else:
            self.redirect('/login')
