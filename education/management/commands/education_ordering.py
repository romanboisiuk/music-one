from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand

from education.api.serializers.card_ordering import CardOrderingSerializer
from education.models.quest_structure import (
    EducationLevel,
    QuestGroup,
    Quest,
)
from education.models.quest_structure import (
    LEVEL_EXAM,
    GROUP_TEST,
    QUEST,
    CONGRATS
)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for level in EducationLevel.objects.all():
            level_exam = level.level_exam
            quest_groups = QuestGroup.objects.filter(level=level)
            for group in quest_groups:
                quests = Quest.objects.filter(group__pk=group.pk).values()
                for quest in quests:
                    quest_obj = CardOrderingSerializer(data={
                        'card_id': quest['id'],
                        'card_type': QUEST
                    })
                    self.check_and_save(quest_obj)
                try:
                    group_test = group.group_test
                except ObjectDoesNotExist:
                    continue
                    
                group_test_obj = CardOrderingSerializer(data={
                    'card_id': group_test.id,
                    'card_type': GROUP_TEST
                })
                self.check_and_save(group_test_obj)
            level_exam_obj = CardOrderingSerializer(data={
                'card_id': level_exam.pk,
                'card_type': LEVEL_EXAM
            })
            self.check_and_save(level_exam_obj)
            congrats_obj = CardOrderingSerializer(data={
                'card_id': level.congrats.pk,
                'card_type': CONGRATS
            })
            self.check_and_save(congrats_obj)

    @staticmethod
    def check_and_save(obj):
        if obj.is_valid():
            obj.save()
