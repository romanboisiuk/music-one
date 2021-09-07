from django.urls import path

from insta_parser.views import InstagramDataView

urlpatterns = [
    path('instagram_data/', InstagramDataView.as_view(), name='instagram_data'),
]
