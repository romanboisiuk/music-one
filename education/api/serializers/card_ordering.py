from rest_framework import serializers

from education.models import CardOrdering


class CardOrderingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardOrdering
        fields = '__all__'
