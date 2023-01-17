import asyncio
import tornado.web
import Index
import Quote
import os.path
import TemplateTest

HTMLDIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__),
                 "..","html"
    )
)
#foo

def makeApp():
    endpoints = [
        ("/", Index.Handler),
        ("/quote", Quote.Handler),
        ("/TemplateTest", TemplateTest.Handler)
    ]
    app = tornado.web.Application(endpoints, static_path=HTMLDIR)
    app.listen(8000)
    return app

if __name__ == "__main__":
    app = makeApp()
    asyncio.get_event_loop().run_forever()