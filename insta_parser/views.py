from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from insta_parser.models import *
from insta_parser.serializers import (
    IgtvHashtagsSerializer,
    HighlightSerializer,
    StoryHashtagsSerializer,
    UserInstagramSerializer,
    StorySerializer,
    IgtvSerializer,
)
from main.models import MusicOneUser


class InstagramDataView(APIView):

    def get(self, request):
        igtv_hashtags_queryset = IgtvHashtag.objects.all()
        highlight_queryset = Highlight.objects.all()
        story_hashtags_queryset = StoryHashtag.objects.all()
        users_queryset = MusicOneUser.objects.all()
        users_serializer = UserInstagramSerializer(users_queryset, many=True)
        igtv_hashtags_serializer = IgtvHashtagsSerializer(igtv_hashtags_queryset, many=True)
        highlight_serializer = HighlightSerializer(highlight_queryset, many=True)
        story_hashtags_serializer = StoryHashtagsSerializer(story_hashtags_queryset, many=True)
        return Response({
            'highlights': highlight_serializer.data,
            'users': users_serializer.data,
            'igtv_hashtags': igtv_hashtags_serializer.data,
            'story_hashtags': story_hashtags_serializer.data,
        })

    def post(self, request):
        input_data = request.data
        igtvs = input_data['igtvs']
        stories = input_data['stories']
        igtv_serializer = IgtvSerializer(data=igtvs, many=True)
        story_serializer = StorySerializer(data=stories, many=True)
        if igtv_serializer.is_valid():
            igtv_serializer.save()
        else:
            return Response(igtv_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if story_serializer.is_valid():
            story_serializer.save()
        else:
            return Response(story_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({}, status=status.HTTP_201_CREATED)
