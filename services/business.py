from repositories.business.repository_interface import *
from services.permissions import PermissionsService
from services.registration import RegistrationService


class BusinessService:
    def __init__(self, business_repository: BusinessRepositoryInterface,
                 permissions_service: PermissionsService,
                 registration_service: RegistrationService):
        self.business_repository = business_repository
        self.permissions_service = permissions_service
        self.registration_service = registration_service

    # admin actions
    def course_creation(self, request: CourseCreationRequest):
        if not self.permissions_service.is_admin(request.author_id):
            raise Exception("author of the request is not a admin")
        self.business_repository.course_creation(request)

    def add_students_to_course(self, request: AddStudentsToCourseRequest):
        if not self.permissions_service.is_admin(request.author_id):
            raise Exception("author of the request is not a admin")
        for user_id in request.users_id:
            if not self.registration_service.user_exists(user_id):
                raise Exception(f"the user with {user_id} id does not exist")
        self.business_repository.add_students_to_course(request)

    # lecturer actions
    def class_creation(self, request: ClassCreationRequest):
        if not self.permissions_service.is_lecturer(request.author_id):
            raise Exception("author of the request is not a lecturer")
        self.business_repository.class_creation(request)

    def add_students_to_class(self, request: AddStudentsToClassRequest):
        self.business_repository.add_students_to_class(request)

    def add_mark_formula_unit(self, request: MarkFormulaUnitCreationRequest):
        self.business_repository.add_mark_formula_unit(request)

    def add_unit_to_class(self, request: UnitCreationRequest):
        self.business_repository.add_unit_to_class(request)

    def add_mark(self, request: MarkCreationRequest):
        self.business_repository.add_mark(request)
