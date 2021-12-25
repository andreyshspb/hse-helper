from pydantic import BaseModel


class AddLecturerRequest(BaseModel):
    author_id: int  # a request author id
    user_id: int
