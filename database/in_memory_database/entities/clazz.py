from typing import List

from requests.class_creation import ClassCreationRequest
from requests.mark_formula_unit_creation import MarkFormulaUnitCreationRequest
from requests.unit_creation import UnitCreationRequest


class MarkFormulaUnit:
    def __init__(self, request: MarkFormulaUnitCreationRequest):
        pass

    def add_unit(self, request: UnitCreationRequest):
        pass


class Class:

    def __init__(self, request: ClassCreationRequest):
        self.students = list()
        self.mark_formula_units = list()

    def add_students(self, users_id: List[int]):
        self.students = self.students + users_id

    def add_mark_formula_unit(self, request: MarkFormulaUnitCreationRequest):
        self.mark_formula_units.append(MarkFormulaUnit(request))

    def get_mark_formula_unit(self, mark_formula_unit_id) -> MarkFormulaUnit:
        if len(self.mark_formula_units) <= mark_formula_unit_id:
            raise Exception("mark_formula_unit with specified id does not exist")
        return self.mark_formula_units[mark_formula_unit_id]
