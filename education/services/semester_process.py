from education.models.semester import Semester
from education.models.user_education_status import UserEducationStatus, SemesterProgress, FAILED, FINISHED
from main.models.user_info import MusicOneUser, STUDENT
from education.models.card_ordering import CONGRATS


class SemesterService:
    def start_semester(self):
        active_students = MusicOneUser.objects.filter(
            is_active=True,
            role=STUDENT
        ).values_list('pk', flat=True)
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

    def finish_semester(self):
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
        current_semester = Semester()
        current_semester.status = FINISHED
        current_semester.save()
