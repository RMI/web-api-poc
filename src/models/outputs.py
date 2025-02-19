from pydantic import BaseModel

class mtcar(BaseModel): 
    mpg: float
    cyl: int
    disp: float
    hp: int
    drat: float
    wt: float
    qsec: float
    vs: bool
    am: bool
    gear: int
    carb: int

