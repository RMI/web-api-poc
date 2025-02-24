from fastapi import APIRouter, status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models.outputs import mtcar
from services.mtcars import MTCARS

data_output = APIRouter()


@data_output.get(
    # api endpoint for complete mtcars dataset
    "/api/dataset",
    tags=["data"],
    summary="Return mtcars dataset ",
    response_description="mtcars dataset in json",
    status_code=status.HTTP_200_OK,
    response_model=mtcar,
)
async def get_full_mtcars() -> mtcar:
    # convert MTCARS dict into JSON response
    MTCARS_json = jsonable_encoder(MTCARS)
    return JSONResponse(content=MTCARS_json)


@data_output.get(
    # api endpoint for individual mtcars items
    "/api/{item_id}",
    tags=["data"],
    summary="Return mtcars item",
    response_description="mtcars item in json",
    status_code=status.HTTP_200_OK,
    response_model=mtcar,
)
async def read_item(item_id: str):
    if item_id not in MTCARS:
        raise HTTPException(status_code=404, detail="Item not found")

    return MTCARS[item_id]
