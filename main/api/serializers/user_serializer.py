from rest_framework import serializers

from main.models.user_info import MusicOneUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MusicOneUser
        fields = ('first_name', 'last_name')
