from django.core.management.base import BaseCommand

from education.models.semester import Semester, IN_PROGRESS
from education.models.user_education_status import SemesterProgress, FAILED, FINISHED
from main.models import MusicOneUser, STUDENT


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        active_students = MusicOneUser.objects.filter(
            is_active=True,
            role=STUDENT
        )
        for student in active_students:
            obj = SemesterProgress()
            obj.user = student
            try:
                semester_progress = SemesterProgress.objects.get(user=student)
            except SemesterProgress.DoesNotExist:
                obj.education_level = 1
            else:
                current_education_level = semester_progress.education_level
                prev_semester_status = semester_progress.status
                if prev_semester_status == FAILED:
                    obj.education_level = current_education_level
                elif prev_semester_status == FINISHED:
                    if current_education_level > 9:
                        continue

                    obj.education_level = current_education_level + 1

            obj.save()

        current_semester = Semester.objects.last()
        current_semester.status = IN_PROGRESS
        current_semester.save()
