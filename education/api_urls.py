from django.urls import path

from education.api.views.education_level import UserCardView

urlpatterns = [
    path('user_card/', UserCardView.as_view(), name='user_card'),
]
