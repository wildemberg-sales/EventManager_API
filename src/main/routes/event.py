from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from datetime import datetime

event_route = APIRouter(prefix="/events")

@event_route.get("/")
def get():
    data = [{"message":"eu sou foda", "date": datetime.now()}, {"teste": "sou fodão", "date": datetime.now()}]
    return JSONResponse(content=jsonable_encoder(data), status_code=200)
