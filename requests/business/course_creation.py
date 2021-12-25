from pydantic import BaseModel


class CourseCreationRequest(BaseModel):
    author_id: int  # a request author id
    year: int
