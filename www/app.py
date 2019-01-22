import logging; logging.basicConfig(level = logging.INFO);
#logging是python内置的标准模块，用于输出运行日志

import asyncio, os
from aiohttp import web
# @acyncio.coroutine 把generator标记成coroutine类型，然后 把这个coroutine 扔到EventLoop中执行

# class aiohttp.web.Response(*, status=200, headers=None, content_type=None, body=None, text=None)
def index(request): 
    return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html')

@asyncio.coroutine
def init():
    app = web.Application()
    app.router.add_route('Get', '/', index)
    srv = yield from loop.create_server(app._make_handler(), '127.0.0.1', 9002)
    logging.info('server started at http://127.0.0.1:9002...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init())
loop.run_forever()
