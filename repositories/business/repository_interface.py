from requests.business.course_creation import CourseCreationRequest
from requests.business.add_students_to_course import AddStudentsToCourseRequest
from requests.business.add_students_to_class import AddStudentsToClassRequest
from requests.business.class_creation import ClassCreationRequest
from requests.business.mark_formula_unit_creation import MarkFormulaUnitCreationRequest
from requests.business.unit_creation import UnitCreationRequest
from requests.business.mark_creation import MarkCreationRequest


class BusinessRepositoryInterface:

    # admin actions
    def course_creation(self, request: CourseCreationRequest):
        raise NotImplemented()

    def add_students_to_course(self, request: AddStudentsToCourseRequest):
        raise NotImplemented()

    # lecturer actions
    def class_creation(self, request: ClassCreationRequest):
        raise NotImplemented()

    def add_students_to_class(self, request: AddStudentsToClassRequest):
        raise NotImplemented()

    def add_mark_formula_unit(self, request: MarkFormulaUnitCreationRequest):
        raise NotImplemented()

    def add_unit_to_class(self, request: UnitCreationRequest):
        raise NotImplemented()

    def add_mark(self, request: MarkCreationRequest):
        raise NotImplemented()
