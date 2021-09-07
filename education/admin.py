from django.contrib import admin
from education.models.quest_structure import *
from education.models.semester import *


class EducationLevelAdmin(admin.ModelAdmin):
    pass


admin.site.register(EducationLevel, EducationLevelAdmin)


class LevelExamAdmin(admin.ModelAdmin):
    pass


admin.site.register(LevelExam, LevelExamAdmin)


class LevelExamQuestionAdmin(admin.ModelAdmin):
    pass


admin.site.register(LevelExamQuestion, LevelExamQuestionAdmin)


class LevelExamAnswerVariantAdmin(admin.ModelAdmin):
    pass


admin.site.register(LevelExamAnswerVariant, LevelExamAnswerVariantAdmin)


class QuestGroupAdmin(admin.ModelAdmin):
    pass


admin.site.register(QuestGroup, QuestGroupAdmin)


class QuestAdmin(admin.ModelAdmin):
    pass


admin.site.register(Quest, QuestAdmin)


class GroupTestAdmin(admin.ModelAdmin):
    pass


admin.site.register(GroupTest, GroupTestAdmin)


class GroupTestQuestionAdmin(admin.ModelAdmin):
    pass


admin.site.register(GroupTestQuestion, GroupTestQuestionAdmin)


class GroupTestAnswerVariantAdmin(admin.ModelAdmin):
    pass


admin.site.register(GroupTestAnswerVariant, GroupTestAnswerVariantAdmin)


class QuestQuestionAdmin(admin.ModelAdmin):
    pass


admin.site.register(QuestQuestion, QuestQuestionAdmin)


class QuestAnswerVariantAdmin(admin.ModelAdmin):
    pass


admin.site.register(QuestAnswerVariant, QuestAnswerVariantAdmin)


class SemesterAdmin(admin.ModelAdmin):
    pass


admin.site.register(Semester, SemesterAdmin)
