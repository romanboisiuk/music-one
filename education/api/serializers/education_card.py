from rest_framework import serializers, viewsets
from education.models.quest_structure import (
    LevelExam,
    GroupTest,
    Quest,
)


class LevelExamSerializer(serializers.ModelSerializer):
    level = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = LevelExam
        fields = '__all__'


class GroupTestSerializer(serializers.ModelSerializer):
    level = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = GroupTest
        fields = '__all__'


class QuestSerializer(serializers.ModelSerializer):
    level = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Quest
        fields = '__all__'
