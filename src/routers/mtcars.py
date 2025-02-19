from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models.outputs import mtcar
from services.mtcars import MTCARS

data_output = APIRouter()


@data_output.get(
    "/data",
    tags=["data"],
    summary="Return mtcars dataset ",
    response_description="mtcars dataset in json",
    status_code=status.HTTP_200_OK,
    response_model=mtcar,
) 
async def get_full_mtcars() -> mtcar:
    """
    ## Return mtcars dataset
    Endpoint to return mtcars dataset in json format. 
    Returns:
        mtcars in json format
    """
    
    # convert MTCARS dict into JSON response
    MTCARS_json = jsonable_encoder(MTCARS)
    return JSONResponse(content=MTCARS_json)