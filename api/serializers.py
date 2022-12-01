from rest_framework import serializers
from .models import User, Turf, Image, Schedule


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class TurfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turf
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class ScheduleSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="user.name", read_only=True)

    class Meta:
        model = Schedule
        fields = "__all__"
