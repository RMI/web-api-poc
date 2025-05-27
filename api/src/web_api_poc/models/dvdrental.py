from pydantic import BaseModel, Field
from typing import List, Optional, Any


class Column(BaseModel):
    column_name: str
    data_type: str
    is_nullable: str


class TableList(BaseModel):
    tables: List[str]


class Film(BaseModel):
    film_id: int
    title: str
    description: Optional[str] = None
    release_year: Optional[int] = None
    length: Optional[int] = None
    rating: Optional[str] = None
    rental_rate: Optional[float] = Field(None, description="The cost to rent this film")


class FilmList(BaseModel):
    films: List[Film]
    total: int = Field(..., description="Total number of films matching the criteria")
    limit: int
    skip: int


class Rental(BaseModel):
    rental_id: int
    title: str
    rental_date: Any  # Using Any for timestamp with timezone
    return_date: Optional[Any] = None
    amount: Optional[float] = None
    payment_date: Optional[Any] = None


class RentalList(BaseModel):
    rentals: List[Rental]
    total: int
    limit: int
    skip: int


class Actor(BaseModel):
    actor_id: int
    first_name: str
    last_name: str


class ActorList(BaseModel):
    actors: List[Actor]
    total: int
    limit: int
    skip: int
