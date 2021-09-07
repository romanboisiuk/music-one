from django.urls import path

from main.api.views.views import UsersView

urlpatterns = [
    path('users/<slug:role>/', UsersView.as_view(), name='user'),
]
