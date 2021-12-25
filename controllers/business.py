from services.business import *


def start_business_restapi(application, business_service: BusinessService):

    # admin actions
    @application.post("/course/creation")
    async def course_creation(request: CourseCreationRequest):
        business_service.course_creation(request)

    @application.post("/add/students/to/course")
    async def add_students_to_course(request: AddStudentsToCourseRequest):
        business_service.add_students_to_course(request)

    # lecturer actions
    @application.post("/class/creation")
    async def class_creation(request: ClassCreationRequest):
        business_service.class_creation(request)

    @application.post("/add/students/to/class")
    async def add_students_to_class(request: AddStudentsToClassRequest):
        business_service.add_students_to_class(request)

    @application.post("/add/mark/formula/unit")
    async def add_mark_formula_unit(request: MarkFormulaUnitCreationRequest):
        business_service.add_mark_formula_unit(request)

    @application.post("/add/unit/to/class")
    async def add_unit_to_class(request: UnitCreationRequest):
        business_service.add_unit_to_class(request)

    @application.post("/add/mark")
    async def add_mark(request: MarkCreationRequest):
        business_service.add_mark(request)
