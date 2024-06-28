from aiohttp import web

async def web_server():
    app = web.Application()
    # Define your routes here, for example:
    app.router.add_get('/', hello)
    return app

async def hello(request):
    return web.Response(text="https://github.com/AshutoshGoswami24 && https://github.com/SudoR2spr")
