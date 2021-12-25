from typing import List

from repositories.registration.repository_interface import *
from repositories.registration.in_memory.entities.user import User


class RegistrationInMemoryRepository:
    users: List[User] = list()

    def register_user(self, request: UserRegistrationRequest):
        self.users.append(User(request))

    def get_user(self, user_id: int) -> UserInformationResponse:
        if len(self.users) <= user_id:
            raise Exception("the user with the specified id does not exist")
        return self.users[user_id].to_user_information_response()

    def user_exists(self, user_id: int) -> bool:
        return 0 <= user_id < len(self.users)
