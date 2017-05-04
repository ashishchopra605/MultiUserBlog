
from webapp2 import WSGIApplication
from google.appengine.ext import db

from main import *

from models.user import User
from models.post import Post
from models.like import Like
from models.comment import comment

from handlers.blogfront import BlogFront
from handlers.bloghandle import BlogHandler
from handlers.deletecomment import DeleteComment
from handlers.deletepost import DeletePost
from handlers.editcomment import EditComment
from handlers.editpost import EditPost
from handlers.like import LikeHandler
from handlers.login import Login
from handlers.logout import Logout
from handlers.mainpage import MainPage
from handlers.newpost import NewPost
from handlers.postcomment import PostComment
from handlers.postpage import PostPage
from handlers.signup import Signup
from handlers.register import Register
from handlers.userpage import UserPage


app = webapp2.WSGIApplication([('/', MainPage),
                               ('/blog', BlogFront),
                               ('/blog/([0-9]+)', PostPage),
                               ('/blog/newpost', NewPost),
                               ('/signup', Register),
                               ('/login', Login),
                               ('/logout', Logout),
                               ('/blog/user', UserPage),
                               ('/like/([0-9]+)', LikeHandler),
                               ('/postcomment/([0-9]+)', PostComment),
                               ('/editcomment/([0-9]+)/([0-9]+)', EditComment),
                               ('/deletecomment/([0-9]+)', DeleteComment),
                               ('/editpost/([0-9]+)', EditPost),
                               ('/deletepost/([0-9]+)', DeletePost),
                               ],
                              debug=True)
