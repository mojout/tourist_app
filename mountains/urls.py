from rest_framework import routers
from .views import Mountainsviewset
from django.urls import path, include
from .yasg import urlpatterns as doc_urls

router = routers.DefaultRouter()
router.register(r'submitdata', Mountainsviewset, basename='submitdata')

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += doc_urls
