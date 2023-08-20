from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from django_filters import rest_framework as df_filters
from rest_framework.permissions import AllowAny

from .serializers import MountainSerializer
from .models import Mountain


class MountainFilter(df_filters.FilterSet):
    class Meta:
        model = Mountain
        fields = ['user__email']


class Mountainsviewset(viewsets.ModelViewSet):
    queryset = Mountain.objects.all().prefetch_related('user', 'coords', 'level', 'images')
    serializer_class = MountainSerializer
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']
    filter_backends = [df_filters.DjangoFilterBackend]
    filterset_class = MountainFilter
    permission_classes = (AllowAny, )

    def update(self, request, *args, **kwargs):
        mountain = self.get_object()
        serializer = self.get_serializer(mountain, data=request.data, partial=True)
        if serializer.is_valid():
            if mountain.status != "NEW":
                raise ValidationError("Stotus is not 'New'. It is allowed to edit a post only in the 'New' status")
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


