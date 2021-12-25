from services.registration import *


def start_registration_restapi(application, registration_service: RegistrationService):

    @application.post("/register/user")
    async def register_user(request: UserRegistrationRequest):
        registration_service.register_user(request)

    @application.get("/get/user")
    async def get_user(user_id: int) -> UserInformationResponse:
        return registration_service.get_user(user_id)
