import tornado.web
import random

quotes = [
    "The odifsoidfj",
    "alksdfslkdf",
    "KJKJHafsd",
    "kajhfksajhdf"
]

class Handler(tornado.web.RequestHandler):
    def get(self):
        q = random.choice(quotes)
        self.write(
            f'<img src = "/static/Quotes.png"><br>{q}'
        )