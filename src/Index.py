import tornado.web
import time




class Handler(tornado.web.RequestHandler):
    
    def get(self):
        self.write('<a href="/quote">Press to get a quote</a>')
        # now = time.ctime()
        self.write(" ".join([" ---The current date and time is: ---", time.ctime()]))
        