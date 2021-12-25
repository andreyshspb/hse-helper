from pydantic import BaseModel


class UserRegistrationRequest(BaseModel):
    author_id: int  # a request author id
    name: str
