from fastapi import APIRouter
from src.http_types.http_request import HttpRequest
from src.validators.events_link_creator_validator import EventsLinkCreatorBaseModel
from src.controllers.events_link.events_links_creator import EventsLinkCreator
from src.model.repositories.eventos_link_repository import EventosLinkRepository

events_link_route = APIRouter(prefix="/events-link")

@events_link_route.post("/")
async def post(request: EventsLinkCreatorBaseModel):
    http_request = HttpRequest(body=request)
    
    events_link_repo = EventosLinkRepository()
    events_creator = EventsLinkCreator(events_link_repo)
    response = events_creator.create(http_request)
    
    return response.get_response()
