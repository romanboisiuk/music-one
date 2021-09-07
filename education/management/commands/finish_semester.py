from django.core.management.base import BaseCommand

from education.constants import CONGRATS
from education.models.semester import Semester
from education.models.user_education_status import (
    SemesterProgress,
    FAILED,
    FINISHED,
    UserEducationStatus,
)
from main.models import MusicOneUser, STUDENT


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        active_students = MusicOneUser.objects.filter(
            is_active=True,
            role=STUDENT
        ).values_list('pk', flat=True)
        for student in active_students:
            semester_progress = SemesterProgress.objects.get(user=student)
            current_card = UserEducationStatus.objects.get(user=student).current_card
            if current_card.card_type == CONGRATS:
                semester_progress.status = FINISHED
            else:
                semester_progress.status = FAILED
            semester_progress.save()
        current_semester = Semester.objects.last()
        current_semester.status = FINISHED
        current_semester.save()
