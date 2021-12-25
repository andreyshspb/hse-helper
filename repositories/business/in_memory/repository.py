from typing import Dict, List

from repositories.business.repository_interface import *

from repositories.business.in_memory.entities.course import Course
from repositories.business.in_memory.entities.clazz import Class


class BusinessInMemoryRepository(BusinessRepositoryInterface):
    courses: Dict[int, Course] = dict()
    classes: List[Class] = list()

    # admin actions
    def course_creation(self, request: CourseCreationRequest):
        if request.year in self.courses:
            raise Exception("course with the specified year already exists")
        self.courses[request.year] = Course(request.year)

    def add_students_to_course(self, request: AddStudentsToCourseRequest):
        if not request.year in self.courses:
            raise Exception("course with the specified year does not exist")
        course = self.courses[request.year]
        course.add_students(request.users_id)

    # lecturer actions
    def class_creation(self, request: ClassCreationRequest):
        clazz = Class(request)
        self.classes.append(clazz)

    def add_students_to_class(self, request: AddStudentsToClassRequest):
        self.__check_class_existence(request.class_id)
        clazz = self.classes[request.class_id]
        clazz.add_students(request.users_id)

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
