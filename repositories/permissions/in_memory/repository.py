from typing import Set

from repositories.permissions.repository_interface import *


class PermissionsInMemoryRepository(PermissionsRepositoryInterface):
    admins: Set[int] = set()
    lecturers: Set[int] = set()

    # permissions actions
    def is_admin(self, user_id: int) -> bool:
        return user_id in self.admins

    def is_lecturer(self, user_id: int) -> bool:
        return user_id in self.lecturers

    # add permissions
    def add_admin(self, request: AddAdminRequest):
        self.admins.add(request.user_id)

    def add_lecturer(self, request: AddLecturerRequest):
        self.lecturers.add(request.user_id)
