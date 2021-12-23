from requests.user_registration import UserRegistrationRequest
from responses.user_information import UserInformationResponse


class User:
    def __init__(self, request: UserRegistrationRequest):
        self.name = request.name

    def to_user_information_response(self) -> UserInformationResponse:
        response = UserInformationResponse()
        response.name = self.name
        return response
