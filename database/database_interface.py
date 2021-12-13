from typing import List

from requests.class_creation import ClassCreationRequest
from requests.mark_formula_unit_creation import MarkFormulaUnitCreationRequest
from requests.unit_creation import UnitCreationRequest
from requests.mark_creation import MarkCreationRequest


class DatabaseInterface:

    # admin actions
    def course_creation(self, year: int):
        raise NotImplemented()

    def add_students_to_course(self, year: int, users_id: List[int]):
        raise NotImplemented()

    def add_lecturer(self, user_id: int):
        raise NotImplemented()

    # lecturer actions
    def class_creation(self, request: ClassCreationRequest):
        raise NotImplemented()

    def add_students_to_class(self, class_id: int, users_id: List[int]):
        raise NotImplemented()

    def add_helper_to_course(self, user_id: int, class_id: int):
        raise NotImplemented()

    def add_mark_formula_unit(self, request: MarkFormulaUnitCreationRequest):
        raise NotImplemented()

    def add_unit_to_class(self, request: UnitCreationRequest):
        raise NotImplemented()

    def add_mark(self, request: MarkCreationRequest):
        raise NotImplemented()
