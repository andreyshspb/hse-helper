from pydantic import BaseModel


class UserRegistrationRequest(BaseModel):
    name: str
