from handlers.bloghandle import BlogHandler


class MainPage(BlogHandler):
    """Redirect to front page """
    def get(self):
        self.redirect('/blog')
