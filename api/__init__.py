from . import login

def add_routers(app):
    app.include_router(login.router)

    