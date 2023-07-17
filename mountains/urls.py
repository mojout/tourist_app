from rest_framework import routers
from .views import Mountainsviewset
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'submitdata', Mountainsviewset, basename='submitdata')

urlpatterns = [
    path('', include(router.urls)),
]