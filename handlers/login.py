from google.appengine.ext import db
from handlers.bloghandle import BlogHandler
from models.user import User
import main


class Login(BlogHandler):
    """Handler for Login"""
    def get(self):
        self.render('login-form.html')

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        u = User.login(username, password)
        if u:
            self.login(u)
            self.redirect('/blog/user')
        else:
            msg = 'Invalid login'
            self.render('login-form.html', error=msg)
