from fastapi import APIRouter
from src.http_types.http_request import HttpRequest
from src.validators.subscriber_creator_validator import SubscriberCreatorBaseModel
from src.controllers.subscribers.subscribers_creator import SubscriberCreator
from src.model.repositories.subscribers_repository import SubscribersRepository

subs_route = APIRouter(prefix="/subs")

@subs_route.post("/")
async def post(request: SubscriberCreatorBaseModel):
    http_request = HttpRequest(body=request)
    
    subs_repo = SubscribersRepository()
    subs_creator = SubscriberCreator(subs_repo)
    response = subs_creator.create(http_request)
    
    return response.get_response()
