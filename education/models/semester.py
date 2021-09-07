from django.db import models

IN_PROGRESS = 'in_progress'
FINISHED = 'finished'
NOT_STARTED = 'not_started'

SEMESTER_STATUS = (
    (IN_PROGRESS, IN_PROGRESS),
    (FINISHED, FINISHED),
    (NOT_STARTED, NOT_STARTED),
)


class Semester(models.Model):
    status = models.CharField(
        choices=SEMESTER_STATUS,
        max_length=11,
        default=NOT_STARTED
    )
    year = models.IntegerField()
    number = models.IntegerField(
        choices=((1, 1), (2, 2))
    )
    start = models.DateField()
    finish = models.DateField()

    def __str__(self):
        return f'{self.year} {self.number} {self.status}'
