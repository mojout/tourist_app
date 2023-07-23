from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import MountainSerializer, ImageSerializer
from .models import Mountain, MountainImage


class Mountainsviewset(viewsets.ModelViewSet):
    queryset = Mountain.objects.all().prefetch_related('user', 'coords', 'level', 'images')
    serializer_class = MountainSerializer
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']

    def update(self, request, *args, **kwargs):
        mountain = self.get_object()
        serializer = self.get_serializer(mountain, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'state': 1,
                'message': 'The record was successfully updated'
            })

        else:
            return Response({
                'state': 0,
                'message': serializer.errors
            })
