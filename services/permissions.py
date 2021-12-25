from repositories.permissions.repository_interface import *
from services.registration import RegistrationService


class PermissionsService:
    def __init__(self, permissions_repository: PermissionsRepositoryInterface,
                 registration_repository: RegistrationService):
        self.permissions_repository = permissions_repository
        self.registration_repository = registration_repository

    # permissions actions
    def is_admin(self, user_id: int) -> bool:
        return self.permissions_repository.is_admin(user_id)

    def is_lecturer(self, user_id: int) -> bool:
        return self.permissions_repository.is_lecturer(user_id)

    # add permissions
    def add_admin(self, request: AddAdminRequest):
        if not self.is_admin(request.author_id):
            raise Exception("author of the request is not a admin")
        if not self.registration_repository.user_exists(request.user_id):
            raise Exception("the specified user id does not exist")
        self.permissions_repository.add_admin(request.user_id)

    def add_lecturer(self, request: AddAdminRequest):
        if not self.is_admin(request.author_id):
            raise Exception("the request author is not a admin")
        if not self.registration_repository.user_exists(request.user_id):
            raise Exception("the specified user id does not exist")
        self.permissions_repository.add_lecturer(request.user_id)
