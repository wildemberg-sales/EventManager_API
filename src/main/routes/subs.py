from fastapi import APIRouter
from src.http_types.http_request import HttpRequest
from src.validators.subscriber_creator_validator import SubscriberCreatorBaseModel
from src.controllers.subscribers.subscribers_creator import SubscriberCreator
from src.model.repositories.subscribers_repository import SubscribersRepository
from src.controllers.subscribers.subscribers_manager import SubscriberManager

subs_route = APIRouter(prefix="/subs")

@subs_route.post("/")
async def post(request: SubscriberCreatorBaseModel):
    http_request = HttpRequest(body=request)
    
    subs_repo = SubscribersRepository()
    subs_creator = SubscriberCreator(subs_repo)
    response = subs_creator.create(http_request)
    
    return response.get_response()

@subs_route.get("/link/{link}/event/{event_id}")
def subscribers_by_link(link:str, event_id:int):
    http_request = HttpRequest(param={"link":link, "event_id":event_id})
    
    subs_repo = SubscribersRepository()
    subs_manager = SubscriberManager(subs_repo)
    
    response = subs_manager.get_subscribers_by_link(http_request)
    
    return response.get_response()

@subs_route.get("/ranking/event/{event_id}")
def subscribers_get_ranking(event_id:int):
    http_request = HttpRequest(param={"event_id":event_id})
    
    subs_repo = SubscribersRepository()
    subs_manager = SubscriberManager(subs_repo)
    
    response = subs_manager.get_events_ranking(http_request)
    
    return response.get_response()