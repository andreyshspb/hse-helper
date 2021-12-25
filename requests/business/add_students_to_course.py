from pydantic import BaseModel

from typing import List


class AddStudentsToCourseRequest(BaseModel):
    author_id: int  # a request author id
    year: int
    users_id: List[int]
