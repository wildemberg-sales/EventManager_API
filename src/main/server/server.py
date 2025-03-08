from fastapi import FastAPI
from src.main.routes.event import event_route
from src.main.routes.subs import subs_route

def create_fastapi_app():
    app = FastAPI()
    app.include_router(event_route)
    app.include_router(subs_route)
    
    return app

api = create_fastapi_app()