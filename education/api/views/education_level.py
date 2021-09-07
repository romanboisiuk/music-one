from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.services.registry import ServiceRegistry
from education.api.mixins.card_permission import CardPermissionMixin

from education.models.quest_structure import (
    LEVEL_EXAM,
    GROUP_TEST,
    QUEST,
)

from education.api.serializers.mark_serializer import (
    QuestMarkSerializer,
    TestMarkSerializer,
    LevelExamMarkSerializer,
)

MARK_SERIALIZERS = {
    LEVEL_EXAM: LevelExamMarkSerializer,
    GROUP_TEST: TestMarkSerializer,
    QUEST: QuestMarkSerializer
}


class UserCardView(APIView, CardPermissionMixin):
    permission_classes = (CardPermissionMixin,)
    service = ServiceRegistry.education_service()

    def get(self, request, *args, **kwargs):
        card_data = self.service.get_all_questions_by_card(request=request)
        return Response(card_data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):

        card_object_data = self.service.test_checker(user_result=request.data, user=request.user)
        print(card_object_data)
        # serializer = MARK_SERIALIZERS[data['type']](data=card_object_data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)
