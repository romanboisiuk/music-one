from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models.user_info import MusicOneUser
from main.api.serializers.user_serializer import UserSerializer


class UsersView(APIView):

    def get(self, request, role, *args, **kwargs):
        queryset = MusicOneUser.objects.filter(
            Q(is_active=True) &
            Q(role=role)
        ).order_by('total_mark').values_list('first_name', 'last_name', 'total_mark')
        data = [
            {
                '№': index,
                'name': f'{data[0]} {data[1]}',
                'total_mark': data[2]
            } for index, data in enumerate(queryset, 1)
        ]
        return Response(
            data=data,
            status=status.HTTP_200_OK
        )
