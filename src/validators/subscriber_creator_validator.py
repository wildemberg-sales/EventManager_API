from pydantic import BaseModel, Field
from typing import Optional

class SubscriberCreatorDataModel(BaseModel):
    name: str = Field(..., min_length=1)
    email: str = Field(..., min_length=1)
    link: Optional[str] = Field(..., min_length=1)
    evento_id: int = Field(..., gt=0)

class SubscriberCreatorBaseModel(BaseModel):
    data: SubscriberCreatorDataModel