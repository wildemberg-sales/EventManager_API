from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from datetime import datetime
from src.http_types.http_response import HttpResponse
from src.http_types.http_request import HttpRequest

event_route = APIRouter(prefix="/events")

@event_route.get("/")
async def get(request: Request):
    http_request = HttpRequest(body=await request.json())
    
    http_response = HttpResponse(body=http_request.body, status_code=200)
    
    return JSONResponse(content=jsonable_encoder(http_response.body), status_code=http_response.status_code)
