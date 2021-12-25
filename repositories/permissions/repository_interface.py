from requests.permissions.add_admin import AddLecturerRequest
from requests.permissions.add_lecturer import AddAdminRequest


class PermissionsRepositoryInterface:

    # permissions actions
    def is_admin(self, user_id: int) -> bool:
        raise NotImplemented()

    def is_lecturer(self, user_id: int) -> bool:
        raise NotImplemented()

    # add permissions
    def add_admin(self, request: AddAdminRequest):
        raise NotImplemented()

    def add_lecturer(self, request: AddLecturerRequest):
        raise NotImplemented()
