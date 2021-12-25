from requests.permissions.is_admin import IsAdminRequest
from requests.permissions.is_lecturer import IsLecturerRequest
from requests.permissions.add_admin import AddLecturerRequest
from requests.permissions.add_lecturer import AddAdminRequest


class PermissionsRepositoryInterface:

    # permissions actions
    def is_admin(self, request: IsAdminRequest) -> bool:
        raise NotImplemented()

    def is_lecturer(self, request: IsLecturerRequest) -> bool:
        raise NotImplemented()

    # add permissions
    def add_admin(self, request: AddAdminRequest):
        raise NotImplemented()

    def add_lecturer(self, request: AddLecturerRequest):
        raise NotImplemented()
