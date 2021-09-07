from django.db import models

from education.models.quest_structure import (
    LEVEL_EXAM,
    GROUP_TEST,
    QUEST,
    CONGRATS,
)

CARD_TYPE_CHOICES = (
    (LEVEL_EXAM, LEVEL_EXAM),
    (GROUP_TEST, GROUP_TEST),
    (QUEST, QUEST),
    (CONGRATS, CONGRATS),
)


class CardOrdering(models.Model):
    card_id = models.IntegerField()
    card_type = models.CharField(
        choices=CARD_TYPE_CHOICES,
        max_length=10
    )

    def __str__(self):
        return str(self.card_id)
