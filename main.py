
# _*_ coding: utf-8 _*_ 
# filename: main.py
import web

from handle import Handle
urls = (
    '/wx', 'Handle',
)


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
