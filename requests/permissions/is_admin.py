from pydantic import BaseModel


class IsAdminRequest(BaseModel):
    author_id: int  # a request author id
    user_id: int
