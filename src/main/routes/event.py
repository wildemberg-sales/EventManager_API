from fastapi import APIRouter
from src.http_types.http_request import HttpRequest
from src.validators.events_creator_validator import EventsCreatorBaseModel
from src.controllers.events.events_creator import EventsCreator
from src.model.repositories.eventos_repository import EventosRepository

event_route = APIRouter(prefix="/events")

@event_route.post("/")
async def post(request: EventsCreatorBaseModel):
    http_request = HttpRequest(body=request)
    
    events_repo = EventosRepository()
    events_creator = EventsCreator(events_repo)
    response = events_creator.create(http_request)
    
    return response.get_response()
