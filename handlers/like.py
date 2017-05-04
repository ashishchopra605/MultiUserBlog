from google.appengine.ext import db
from handlers.bloghandle import BlogHandler
from models.like import Like
from models.post import Post
from main import *
from decorator import *


class LikeHandler(BlogHandler):
    """Handler for Like"""
    @post_exists
    def post(self, post_id, post):
        if user_logged_in(self):
            idpost = post.key().id()
            idpost = int(idpost)
            if not user_owns_post(self, post):
                likeobj = Like.all()
                likeobj.filter('post_id =', idpost)
                likeobj.filter('user_id =', self.user.key().id())
                result = likeobj.get()
                if result:
                    result.delete()
                    post.likes -= 1
                    post.put()
                    time.sleep(0.1)
                    self.redirect('/blog')
                else:
                    likeobj = Like(post_id=idpost,
                                   user_id=self.user.key().id())
                    likeobj.put()
                    post.likes += 1
                    post.put()
                    time.sleep(0.1)
                    self.redirect('/blog')
            else:
                error = "you cannot like your own post"
                self.render("error.html", error=error)
        else:
            self.redirect("/login")
