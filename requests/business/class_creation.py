from pydantic import BaseModel


class ClassCreationRequest(BaseModel):
    author_id: int  # a request author id
    name: str
    description: str
