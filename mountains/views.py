from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import MountainSerializer
from .models import Mountain


class Mountainsviewset(viewsets.ModelViewSet):
    queryset = Mountain.objects.all()
    serializer_class = MountainSerializer
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']


