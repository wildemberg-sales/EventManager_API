from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from src.http_types.http_response import HttpResponse
from src.http_types.http_request import HttpRequest
from src.validators.events_creator_validator import EventsCreatorBaseModel

event_route = APIRouter(prefix="/events")

@event_route.get("/")
async def get(request: EventsCreatorBaseModel):
    http_request = HttpRequest(request.data)
    
    http_response = HttpResponse(body=http_request.body, status_code=200)
    
    return JSONResponse(content=jsonable_encoder(http_response.body), status_code=http_response.status_code)
