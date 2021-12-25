from pydantic import BaseModel


class UnitCreationRequest(BaseModel):
    author_id: int  # a request author id
    class_id: int
    mark_formula_unit_id: int
    name: str
    coefficient: float
