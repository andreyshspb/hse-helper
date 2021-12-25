from pydantic import BaseModel


class ClassCreationRequest(BaseModel):
    author_id: int
    name: str
    description: str
