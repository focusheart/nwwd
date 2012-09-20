# -*- coding=utf-8 -*-

import tornado.ioloop
import tornado.web
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        params = {'title':u"哈哈"}
        self.render('main.html', params=params)

class StoryHandler(tornado.web.RequestHandler):
    def get(self, story_id):
        self.write("You requested the story " + story_id)

handlers = [
    (r"/", MainHandler),
    (r"/story/([0-9]+)", StoryHandler),
]
settings = {
    'debug': True,
    'template_path': os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": "__TODO:this_is_my_secret_phrase_here",
    "login_url": "/login",
    "xsrf_cookies": True,
}
application = tornado.web.Application(handlers, **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
