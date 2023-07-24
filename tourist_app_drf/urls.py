from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mountains.urls')),
    path('swagger-ui/', TemplateView.as_view(
        template_name='../templates/swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('openapi/', get_schema_view(
        title="Tourist app",
        description="Federation of Sports Tourism of Russia application API",
        version="0.1",
    ), name='openapi-schema'),
]
