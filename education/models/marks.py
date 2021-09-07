from django.db import models

from education.models.quest_structure import (
    EducationLevel,
    QuestGroup,
    Quest,
)
from main.models.user_info import MusicOneUser

MARK_TYPE_CHOICES = (
    ('igtv', 'igtv'),
    ('story', 'story'),
)


class QuestMark(models.Model):
    user = models.OneToOneField(
        MusicOneUser,
        on_delete=models.PROTECT
    )
    card = models.ForeignKey(
        Quest,
        on_delete=models.PROTECT
    )
    value = models.IntegerField(default=0)


class TestMark(models.Model):
    user = models.OneToOneField(
        MusicOneUser,
        on_delete=models.PROTECT
    )
    card = models.ForeignKey(
        QuestGroup,
        on_delete=models.PROTECT
    )
    value = models.IntegerField(default=0)


class LevelExamMark(models.Model):
    user = models.OneToOneField(
        MusicOneUser,
        on_delete=models.PROTECT
    )
    card = models.ForeignKey(
        EducationLevel,
        on_delete=models.PROTECT
    )
    mark = models.IntegerField(default=0)


class MediaMark(models.Model):
    user = models.OneToOneField(
        MusicOneUser,
        on_delete=models.PROTECT
    )
    mark = models.IntegerField(default=0)
    mark_type = models.CharField(
        max_length=5,
        choices=MARK_TYPE_CHOICES,
    )
