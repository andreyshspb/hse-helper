from pydantic import BaseModel


class UnitCreationRequest(BaseModel):
    class_id: int
    mark_formula_unit_id: int
    name: str
    coefficient: float
