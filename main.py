from databases.database_interface import DatabaseInterface


def get_database() -> DatabaseInterface:
    return DatabaseInterface()


db = get_database()
