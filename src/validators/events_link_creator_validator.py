from pydantic import BaseModel, Field

class EventsLinkCreatorDataModel(BaseModel):
    event_id: int = Field(..., gt=0),
    inscrito_id: int = Field(..., gt=0)

class EventsLinkCreatorBaseModel(BaseModel):
    data: EventsLinkCreatorDataModel