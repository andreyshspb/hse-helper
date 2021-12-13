from typing import List


from main import db


def course_creation(year: int):
    return db.course_creation(year)


def add_students_to_course(year: int, users_id: List[int]):
    return db.add_students_to_course(year, users_id)


def add_student_to_course(year: int, user_id: int):
    return add_students_to_course(year, [user_id])


def add_lecturer(user_id: int):
    return db.add_lecturer(user_id)
