from django.contrib.auth.models import AnonymousUser
from rest_framework import permissions

from education.models.semester import Semester, IN_PROGRESS
from main.models.user_info import STUDENT


class CardPermissionMixin(permissions.BasePermission):
    def has_permission(self, request, view):
        is_allow = True
        user = request.user
        if isinstance(user, AnonymousUser):
            is_allow = False
        elif user.role != STUDENT or user.is_active is False:
            is_allow = False
        elif self.check_if_semester_started() is False:
            is_allow = False
        return is_allow

    @staticmethod
    def check_if_semester_started():
        try:
            return bool(Semester.objects.get(status=IN_PROGRESS))
        except Semester.DoesNotExist:
            return False
