from pydantic import BaseModel, Field

class EventsCreatorDataModel(BaseModel):
    name: str = Field(..., min_length=1)

class EventsCreatorBaseModel(BaseModel):
    data: EventsCreatorDataModel