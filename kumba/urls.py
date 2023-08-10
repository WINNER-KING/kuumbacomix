from django.contrib import admin
from django.urls import path
from django.contrib.auth import login, logout
from rest_framework_swagger.views import get_swagger_view
from django.contrib.auth import views as authenticate
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Kumba API",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path(r'^login/$', login, name='login'),
    path(r'^logout/$', logout, name='logout'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)