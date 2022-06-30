from django.shortcuts import render
from rest_framework import viewsets
from tusk_manager.models import Task, Object, Categories, Service, CustomUser
from tusk_manager.permissions import IsAuthor
from tusk_manager.serializers import TaskSerializer, ObjectSerializer, CategoriesSerializer, ServiceSerializer, \
    UserSerializer, TaskAddSerializer, ObjectAddSerializer


# Работа со всеми объектами
class ObjectsView(viewsets.ModelViewSet):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer


# Отображение объектов прораба
class UserObjectsView(viewsets.ModelViewSet):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        return Object.objects.filter(worker_id=self.request.user)


# Работа с одним объектом
class ObjectView(viewsets.ModelViewSet):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer

    def get_queryset(self):
        return Object.objects.filter(id=self.kwargs.get('pk'))

class AddObjectView(viewsets.ModelViewSet):
    queryset = Object.objects.all()
    serializer_class = ObjectAddSerializer


# Работа со всеми залачами
class TasksView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskAddView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskAddSerializer


# Отображение задач рабочего
class UserTasksView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        return Task.objects.filter(worker_id=self.request.user)


# Работа с одной задачей
class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(id=self.kwargs.get('pk'))


# Отображение задач по категориям
class TaskObjectView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(object=self.kwargs.get('obj'))


# Отображение категорий
class CategoriesView(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


# Отображение услуг по категориям
class ServiceCategoryView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_queryset(self):
        return Service.objects.filter(category=self.kwargs.get('pk'))


# Отображение пользователя по id
class UserView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.kwargs.get('pk'))


# Отображение пользователей по id
class WorkersView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return CustomUser.objects.filter(position__name='Рабочий')
