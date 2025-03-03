from fastapi import FastAPI
from src.main.routes.event import event_route

def create_fastapi_app():
    app = FastAPI()
    app.include_router(event_route)
    
    return app

api = create_fastapi_app()