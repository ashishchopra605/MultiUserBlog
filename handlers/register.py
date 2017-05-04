from google.appengine.ext import db
from handlers.bloghandle import BlogHandler
from models.user import User
from main import *
from handlers.signup import Signup


class Register(Signup):
    """Register User"""
    def done(self):
        # make sure the user doesn't already exist
        u = User.by_name(self.username)
        if u:
            msg = 'That user already exists.'
            self.render('signup-form.html', error_username=msg)
        else:
            u = User.register(self.username, self.password, self.email)
            u.put()

            self.login(u)
            self.redirect('/blog/user')
