from drf_writable_nested import WritableNestedModelSerializer
from rest_framework.exceptions import ValidationError

from .models import Mountain, MountainImage, Coord, User, Level
from rest_framework import serializers


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'second_name', 'last_name', 'email', 'phone']


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['winter', 'summer', 'autumn', 'spring']


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coord
        fields = ['latitude', 'longitude', 'height']


class ImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = MountainImage
        fields = ['id', 'data', 'title']


class MountainSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    user = UsersSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer()
    images = ImageSerializer(many=True)

    class Meta:
        model = Mountain
        fields = ['id', 'beauty_title', 'title', 'other_title', 'connect', 'add_time', 'user', 'coords', 'level',
                  'images', 'status']

    def validate(self, attrs):
        user_data = attrs.get('user')
        if not user_data:
            raise ValidationError("User data error.")

        if self.instance:
            user = self.instance.user
        else:
            try:
                user = User.objects.get(email=user_data.get('email'))
            except User.DoesNotExist:
                user = None

        if user is not None:
            if user.last_name != user_data.get('last_name') or \
               user.first_name != user_data.get('first_name') or\
               user.second_name != user_data.get('second_name') or \
               user.phone != user_data.get('phone'):
                raise ValidationError("User information cannot be changed.")

        super().validate(attrs)

        return attrs
