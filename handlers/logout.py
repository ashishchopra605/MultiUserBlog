from handlers.bloghandle import BlogHandler
import main


class Logout(BlogHandler):
    """Handler for Logout"""
    def get(self):
        self.logout()
        self.redirect('/login')
