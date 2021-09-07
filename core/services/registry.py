class ServiceRegistry:

    @classmethod
    def education_service(cls):
        from education.services.education import EducationService
        return EducationService()
