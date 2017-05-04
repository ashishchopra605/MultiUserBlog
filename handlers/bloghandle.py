import webapp2
from models.user import User
from main import *


class BlogHandler(webapp2.RequestHandler):
    """Define functions for rendering Web Pages"""
    def write(self, *a, **kw):
        """Write to Web Page"""
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        """Render Jinja template"""
        params['user'] = self.user
        return render_str(template, **params)

    def render(self, template, **kw):
        """Write template to Web Page"""
        self.write(self.render_str(template, **kw))

    def set_secure_cookie(self, name, val):
        """Set Cookie"""
        cookie_val = make_secure_val(val)
        self.response.headers.add_header(
            'Set-Cookie',
            '%s=%s; Path=/' % (name, cookie_val))

    def read_secure_cookie(self, name):
        """Return Cookie Value"""
        cookie_val = self.request.cookies.get(name)
        return cookie_val and check_secure_val(cookie_val)

    def login(self, user):
        """Set Cookie after Login"""
        self.set_secure_cookie('user_id', str(user.key().id()))

    def logout(self):
        """Remove Cookie after Logout"""
        self.response.headers.add_header('Set-Cookie', 'user_id=; Path=/')

    def initialize(self, *a, **kw):
        """Initialise Web Page with signed-in user"""
        webapp2.RequestHandler.initialize(self, *a, **kw)
        uid = self.read_secure_cookie('user_id')
        self.user = uid and User.by_id(int(uid))
