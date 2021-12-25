from pydantic import BaseModel

from typing import List


class AddStudentsToClassRequest(BaseModel):
    author_id: int  # a request author id
    class_id: int
    users_id: List[int]
