class PermissionsRepositoryInterface:

    # permissions actions
    def is_admin(self, user_id: int) -> bool:
        raise NotImplemented()

    def is_lecturer(self, user_id: int) -> bool:
        raise NotImplemented()

    # add permissions
    def add_admin(self, user_id: int):
        raise NotImplemented()

    def add_lecturer(self, user_id: int):
        raise NotImplemented()
