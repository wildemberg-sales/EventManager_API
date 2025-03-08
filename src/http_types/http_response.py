from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

class HttpResponse:
    def __init__(self, body: any, status_code: int) -> None:
        self.body = body
        self.status_code = status_code
    
    def get_response(self) -> JSONResponse:
        return JSONResponse(content=jsonable_encoder(self.body), status_code=self.status_code)