from pydantic import BaseModel


class IsLecturerRequest(BaseModel):
    author_id: int  # a request author id
    user_id: int
