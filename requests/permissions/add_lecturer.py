from pydantic import BaseModel


class AddAdminRequest(BaseModel):
    author_id: int  # a request author id
    user_id: int
