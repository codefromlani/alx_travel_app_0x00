# alx_travel_app/alx_travel_app/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

# drf-yasg imports
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="alx_travel_app API",
        default_version='v1',
        description="API documentation for alx_travel_app",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/listings/', include('listings.urls')),  # include the listings app URLs
    # Swagger UI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # Redoc (optional)
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
