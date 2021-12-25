from pydantic import BaseModel


class MarkCreationRequest(BaseModel):
    author_id: int  # a request author id
    user_id: int
    class_id: int
    mark_formula_unit_id: int
    unit_id: int
    mark: int
