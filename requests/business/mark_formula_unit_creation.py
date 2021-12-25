from pydantic import BaseModel


class MarkFormulaUnitCreationRequest(BaseModel):
    class_id: int
    name: str
    coefficient: float
