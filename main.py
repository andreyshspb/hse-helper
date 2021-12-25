from fastapi import FastAPI

import uvicorn

# repository
from repositories.registration.in_memory.repository import *
from repositories.permissions.in_memory.repository import *
from repositories.business.in_memory.repository import *

# service
from services.registration import RegistrationService
from services.permissions import PermissionsService
from services.business import BusinessService

# rest api
from controllers.registration import start_registration_restapi
from controllers.permissions import start_permissions_restapi
from controllers.business import start_business_restapi


def get_application():
    return FastAPI()


application = get_application()

registration_repository = RegistrationInMemoryRepository()
permissions_repository = PermissionsInMemoryRepository()
business_repository = BusinessInMemoryRepository()

registration_service = RegistrationService(registration_repository)
permissions_service = PermissionsService(permissions_repository,
                                         registration_service)
business_service = BusinessService(business_repository,
                                   permissions_service,
                                   registration_service)

start_registration_restapi(application, registration_service)
start_permissions_restapi(application, permissions_service)
start_business_restapi(application, business_service)


if __name__ == "__main__":
    uvicorn.run(application, host="0.0.0.0", port=8000)
