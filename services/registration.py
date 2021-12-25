from repositories.registration.repository_interface import *


class RegistrationService:
    def __init__(self, registration_repository: RegistrationRepositoryInterface):
        self.registration_repository = registration_repository

    def register_user(self, request: UserRegistrationRequest):
        self.registration_repository.register_user(request)

    def get_user(self, user_id: int) -> UserInformationResponse:
        return self.registration_repository.get_user(user_id)
