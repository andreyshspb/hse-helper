from fastapi import FastAPI

import uvicorn

from repositories.registration.in_memory.repository import *
from services.registration import RegistrationService

from controllers.registration import start_registration_restapi


def get_application():
    return FastAPI(title="yes yes yes")


application = get_application()


registration_repository = RegistrationInMemoryRepository()
registration_service = RegistrationService(registration_repository)

start_registration_restapi(application,
                           registration_service)


if __name__ == "__main__":
    uvicorn.run(application, host="0.0.0.0", port=8000)
