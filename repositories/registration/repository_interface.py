from requests.user_registration import UserRegistrationRequest
from responses.user_information import UserInformationResponse


class RegistrationRepositoryInterface:

    def register_user(self, request: UserRegistrationRequest):
        raise NotImplemented()

    def get_user(self, user_id: int) -> UserInformationResponse:
        raise NotImplemented()

    def user_exists(self, user_id: int) -> bool:
        raise NotImplemented()
