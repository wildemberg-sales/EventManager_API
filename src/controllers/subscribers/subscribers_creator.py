from src.model.repositories.interfaces.subscribers_repository import SubscribersRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class SubscriberCreator:
    def __init__(self, subscriber_repo: SubscribersRepositoryInterface):
        self.__subscriber_repo = subscriber_repo
    
    def create(self, http_request: HttpRequest) -> HttpResponse:
        subscriber_info = http_request.body.data
        subscriber_email = subscriber_info.email
        subscriber_evento_id = subscriber_info.evento_id
        
        self.__check_sub(subscriber_email, subscriber_evento_id)
        self.__insert_sub(subscriber_info)
        
        return self.__format_response(subscriber_info)
    
    def __check_sub(self, subscriber_email:str, evento_id: int) -> None:
        response = self.__subscriber_repo.select_subscriber(subscriber_email, evento_id)
        if response: raise Exception("Subscriber Already Exists!")
    
    def __insert_sub(self, subscriber_info: any) -> None:
        self.__subscriber_repo.insert(subscriber_info)
    
    def __format_response(self, subscriber_info: any) -> HttpResponse:
        return HttpResponse(
            body={
                "data":{
                    "Type": "Subscriber",
                    "Count": 1,
                    "attributes":{
                        "subscriber_info": subscriber_info
                    }
                }
            },
            status_code=201
        )