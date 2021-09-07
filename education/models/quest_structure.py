from django.db import models


LEVEL_CHOISES = [(i, i) for i in range(1, 10)]

LEVEL_EXAM = 'level_exam'
GROUP_TEST = 'group_test'
QUEST = 'quest'
CONGRATS = 'congrats'

CARD_TYPE_CHOICES = (
    (LEVEL_EXAM, LEVEL_EXAM),
    (GROUP_TEST, GROUP_TEST),
    (QUEST, QUEST),
)


class EducationLevel(models.Model):
    name = models.PositiveIntegerField(
        unique=True,
        choices=LEVEL_CHOISES,
    )
    theory = models.TextField()

    def __str__(self):
        return str(self.name)


class LevelExam(models.Model):
    level = models.OneToOneField(
        EducationLevel,
        on_delete=models.PROTECT,
        related_name=LEVEL_EXAM
    )
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class LevelExamQuestion(models.Model):
    level = models.OneToOneField(
        LevelExam,
        on_delete=models.PROTECT,
        related_name='questions'
    )
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class LevelExamAnswerVariant(models.Model):
    question = models.ForeignKey(
        LevelExamQuestion,
        on_delete=models.PROTECT,
        related_name='answer_variants',
    )
    name = models.CharField(max_length=500)
    is_correct = models.BooleanField()

    def __str__(self):
        return self.name


class QuestGroup(models.Model):
    level = models.ForeignKey(
        EducationLevel,
        on_delete=models.PROTECT
    )
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class GroupTest(models.Model):
    group = models.OneToOneField(
        QuestGroup,
        on_delete=models.PROTECT,
        related_name=GROUP_TEST
    )
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class GroupTestQuestion(models.Model):
    group = models.OneToOneField(
        GroupTest,
        on_delete=models.PROTECT,
        related_name='questions',
    )
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class GroupTestAnswerVariant(models.Model):
    question = models.ForeignKey(
        GroupTestQuestion,
        on_delete=models.PROTECT,
        related_name='answer_variants',
    )
    name = models.CharField(max_length=500)
    is_correct = models.BooleanField()

    def __str__(self):
        return self.name


class Quest(models.Model):
    name = models.CharField(max_length=500)
    number = models.CharField(max_length=500)
    group = models.ForeignKey(
        QuestGroup,
        on_delete=models.PROTECT,
        related_name='quest'
    )

    def __str__(self):
        return self.name


class QuestQuestion(models.Model):
    quest = models.ForeignKey(
        Quest,
        on_delete=models.PROTECT,
        related_name='questions'
    )
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class QuestAnswerVariant(models.Model):
    question = models.ForeignKey(
        QuestQuestion,
        on_delete=models.PROTECT,
        related_name='answer_variants',
    )
    name = models.CharField(max_length=500)
    is_correct = models.BooleanField()

    def __str__(self):
        return self.name


class CongratsCard(models.Model):
    education_level = models.ForeignKey(
        EducationLevel,
        on_delete=models.PROTECT,
        related_name='congrats',
    )
