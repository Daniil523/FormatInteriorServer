from django.contrib.auth.models import AbstractUser
from rest_framework import serializers
from tusk_manager.models import CustomUser, Task, Object, Categories, Service, Unit, Material, Position


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'


class MaterialSerializer(serializers.ModelSerializer):
    unit = UnitSerializer(read_only=True)

    class Meta:
        model = Material
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    unit = UnitSerializer(read_only=True)
    material = MaterialSerializer(read_only=True)

    class Meta:
        model = Service
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    position = PositionSerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = ('name', 'description', 'phone', 'url', 'position', 'email', 'id')


class ObjectSerializer(serializers.ModelSerializer):
    worker_id = UserSerializer(read_only=True)

    class Meta:
        model = Object
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)
    object = ObjectSerializer(read_only=True)
    category = CategoriesSerializer(read_only=True)
    worker_id = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'


class ObjectAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = Object
        fields = '__all__'


class TaskAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'