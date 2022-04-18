from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.products.api.v1.urls')),
]

if settings.DEBUG:
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns

if settings.ENABLED_SWAGGER_DOC:
    schema_view = get_schema_view(
        openapi.Info(
            title="Zebrand API",
            default_version='v1',
            description="Zebrand API V1",
            contact=openapi.Contact(email="harol.calzada@gmail.com"),
            license=openapi.License(name="BSD License"),
        ),
        public=True,
        permission_classes=[permissions.AllowAny],
    )
    urlpatterns += [
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
    ]
