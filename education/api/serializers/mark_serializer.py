from rest_framework import serializers, viewsets

from education.models import QuestMark, TestMark, LevelExamMark


class QuestMarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestMark
        fields = '__all__'


class TestMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestMark
        fields = '__all__'


class LevelExamMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelExamMark
        fields = '__all__'
