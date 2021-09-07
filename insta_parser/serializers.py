from rest_framework.serializers import ModelSerializer

from insta_parser.models import *
from main.models import MusicOneUser


class IgtvHashtagsSerializer(ModelSerializer):
    class Meta:
        model = IgtvHashtag
        fields = ['id', 'hash_tag']


class HighlightSerializer(ModelSerializer):
    class Meta:
        model = Highlight
        fields = ['id', 'title']


class StoryHashtagsSerializer(ModelSerializer):
    class Meta:
        model = StoryHashtag
        fields = ['id', 'hash_tag']


class UserInstagramSerializer(ModelSerializer):
    class Meta:
        model = MusicOneUser
        fields = ['id', 'instagram']


class StorySerializer(ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'


class IgtvSerializer(ModelSerializer):
    class Meta:
        model = Igtv
        fields = '__all__'
