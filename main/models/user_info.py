from django.contrib.auth.models import AbstractUser
from django.db import models

STUDENT = 'student'
TEACHER = 'teacher'


class MusicOneUser(AbstractUser):
    ROLE_CHOICES = [
        (STUDENT, STUDENT),
        (TEACHER, TEACHER),
    ]
    instagram = models.URLField(blank=True, null=True)
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default=STUDENT,
    )
    total_mark = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        verbose_name = 'Music One User'
        verbose_name_plural = 'Music One Users'

    def __str__(self):
        return self.username
