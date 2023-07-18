from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import MountainSerializer
from .models import Mountain


class Mountainsviewset(viewsets.ModelViewSet):
    queryset = Mountain.objects.all().prefetch_related('user', 'coords', 'level', 'images')
    serializer_class = MountainSerializer
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']


