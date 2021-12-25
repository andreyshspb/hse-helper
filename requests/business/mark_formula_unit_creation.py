from pydantic import BaseModel


class MarkFormulaUnitCreationRequest(BaseModel):
    author_id: int  # a request author id
    class_id: int
    name: str
    coefficient: float
