from typing import List


class Course:
    def __init__(self, year):
        self.year = year
        self.students = list()

    def __contains__(self, item):
        return item in self.students

    def add_students(self, users_id: List[int]):
        self.students = self.students + users_id
