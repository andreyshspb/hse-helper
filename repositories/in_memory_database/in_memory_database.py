from typing import Dict

from repositories.database_interface import *

from repositories.in_memory_database.entities.course import Course
from repositories.in_memory_database.entities.clazz import Class


class InMemoryDatabase(DatabaseInterface):
    courses: Dict[int, Course] = dict()
    classes: List[Class] = list()

    # rules
    lectures: List[int] = list()
    class_editing: Dict[int, List[int]] = dict()

    # admin actions
    def course_creation(self, year: int):
        if year in self.courses:
            raise Exception("course with the specified year already exists")
        self.courses[year] = Course(year)

    def add_students_to_course(self, year: int, users_id: List[int]):
        if not year in self.courses:
            raise Exception("course with the specified year does not exist")
        course = self.courses[year]
        course.add_students(users_id)

    def add_lecturer(self, user_id: int):
        self.lectures.append(user_id)

    # lecturer actions
    def class_creation(self, request: ClassCreationRequest):
        class_id = len(self.classes)
        clazz = Class(request)
        self.classes.append(clazz)
        self.class_editing[class_id] = [request.class_owner]

    def add_students_to_class(self, class_id: int, users_id: List[int]):
        self.__check_class_existence(class_id)
        clazz = self.classes[class_id]
        clazz.add_students(users_id)

    def add_helper_to_course(self, user_id: int, class_id: int):
        self.__check_class_existence(class_id)
        self.class_editing[class_id].append(user_id)

    def add_mark_formula_unit(self, request: MarkFormulaUnitCreationRequest):
        self.__check_class_existence(request.class_id)
        clazz = self.classes[request.class_id]
        clazz.add_mark_formula_unit(request)

    def add_unit_to_class(self, request: UnitCreationRequest):
        self.__check_class_existence(request.class_id)
        clazz = self.classes[request.class_id]
        clazz.add_unit(request)

    def add_mark(self, request: MarkCreationRequest):
        self.__check_class_existence(request.class_id)
        clazz = self.classes[request.class_id]
        clazz.add_mark(request)

    # helper functions
    def __check_class_existence(self, class_id: int):
        if len(self.classes) <= class_id:
            raise Exception("class with specified id does not exist")

