from typing import Set

from repositories.permissions.repository_interface import PermissionsRepositoryInterface


class PermissionsInMemoryRepository(PermissionsRepositoryInterface):
    admins: Set[int] = set()
    lecturers: Set[int] = set()

    # permissions actions
    def is_admin(self, user_id: int) -> bool:
        return user_id in self.admins

    def is_lecturer(self, user_id: int) -> bool:
        return user_id in self.lecturers

    # add permissions
    def add_admin(self, user_id: int):
        self.admins.add(user_id)

    def add_lecturer(self, user_id: int):
        self.lecturers.add(user_id)
