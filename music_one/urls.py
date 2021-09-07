from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework.authtoken import views


schema_view = get_swagger_view(title='API')


urlpatterns = [
    path('', schema_view),
    path('admin/', admin.site.urls),
    path('api/v1/', include('main.api_urls')),
    path('api/v1/', include('education.api_urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('user/', include('rest_auth.urls')),
    path('parser/', include('insta_parser.urls')),
]
