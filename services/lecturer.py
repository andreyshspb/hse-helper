from typing import List

from requests.class_creation import ClassCreationRequest
from requests.mark_formula_unit_creation import MarkFormulaUnitCreationRequest
from requests.unit_creation import UnitCreationRequest
from requests.mark_creation import MarkCreationRequest

from main import db


def class_creation(request: ClassCreationRequest):
    return db.class_creation(request)


def add_students_to_class(class_id: int, users_id: List[int]):
    return db.add_students_to_class(class_id, users_id)


def add_student_to_class(class_id: int, user_id: int):
    return add_students_to_class(class_id, [user_id])


def add_helper_to_course(user_id: int, class_id: int):
    return db.add_helper_to_course(user_id, class_id)


def add_mark_formula_unit(request: MarkFormulaUnitCreationRequest):
    return db.add_mark_formula_unit(request)


def add_unit_to_class(request: UnitCreationRequest):
    return db.add_unit_to_class(request)


def add_mark(request: MarkCreationRequest):
    return db.add_mark(request)
