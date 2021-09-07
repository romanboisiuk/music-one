from django.db import models

from education.models import LEVEL_CHOISES
from main.models.user_info import MusicOneUser
from education.models.card_ordering import CardOrdering


FINISHED = 'finished'
FAILED = 'failed'
IN_PROGRESS = 'in_progress'

SEMESTER_PROGRESS_STATUS = (
    (FINISHED, FINISHED),
    (FAILED, FAILED)
)


class UserEducationStatus(models.Model):
    user = models.ForeignKey(MusicOneUser, on_delete=models.PROTECT)
    current_card = models.ForeignKey(CardOrdering, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.current_card)


class SemesterProgress(models.Model):
    user = models.ForeignKey(MusicOneUser, on_delete=models.PROTECT)
    education_level = models.IntegerField(choices=LEVEL_CHOISES)
    status = models.CharField(
        max_length=11,
        choices=SEMESTER_PROGRESS_STATUS,
        default=IN_PROGRESS
    )
