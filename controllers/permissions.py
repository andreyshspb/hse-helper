from services.permissions import *


def start_permissions_restapi(application, permissions_service: PermissionsService):

    @application.post("/add/admin")
    async def add_admin(request: AddAdminRequest):
        permissions_service.add_admin(request)

    @application.post("/add/lecturer")
    async def add_lecturer(request: AddLecturerRequest):
        permissions_service.add_lecturer(request)
