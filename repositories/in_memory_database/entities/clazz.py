from typing import Dict, List

from requests.class_creation import ClassCreationRequest
from requests.mark_formula_unit_creation import MarkFormulaUnitCreationRequest
from requests.unit_creation import UnitCreationRequest
from requests.mark_creation import MarkCreationRequest


class Unit:

    def __init__(self, request: UnitCreationRequest):
        self.name: str = request.name
        self.coefficient: float = request.coefficient
        self.marks: Dict[int, int] = dict()

    def add_mark(self, request: MarkCreationRequest):
        if not (0 <= request.mark <= 10):
            raise Exception("mark must be inside the interval [0, 10]")
        self.marks[request.user_id] = request.mark


class MarkFormulaUnit:

    def __init__(self, request: MarkFormulaUnitCreationRequest):
        self.name: str = request.name
        self.coefficient: float = request.coefficient
        self.units: List[Unit] = list()

    def add_unit(self, request: UnitCreationRequest):
        self.units.append(Unit(request))

    def add_mark(self, request: MarkCreationRequest):
        if len(self.units) <= request.unit_id:
            raise Exception("unit with the specified id does not exist")
        unit = self.units[request.unit_id]
        unit.add_mark(request)


class Class:

    def __init__(self, request: ClassCreationRequest):
        self.name: str = request.name
        self.description: str = request.description
        self.students: List[int] = list()
        self.mark_formula_units: List[MarkFormulaUnit] = list()

    def add_students(self, users_id: List[int]):
        self.students = self.students + users_id

    def add_mark_formula_unit(self, request: MarkFormulaUnitCreationRequest):
        self.mark_formula_units.append(MarkFormulaUnit(request))

    def add_unit(self, request: UnitCreationRequest):
        if len(self.mark_formula_units) <= request.mark_formula_unit_id:
            raise Exception("mark formula unit with the specified id does not exist")
        mark_formula_unit = self.mark_formula_units[request.mark_formula_unit_id]
        mark_formula_unit.add_unit(request)

    def add_mark(self, request: MarkCreationRequest):
        if len(self.mark_formula_units) <= request.mark_formula_unit_id:
            raise Exception("mark formula unit with the specified id does not exist")
        mark_formula_unit = self.mark_formula_units[request.mark_formula_unit_id]
        mark_formula_unit.add_mark(request)
