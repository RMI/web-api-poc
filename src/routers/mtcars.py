from fastapi import APIRouter, status
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
        mtcars: Returns a JSON response with the health status
    """
    return {MTCARS(status="OK")}