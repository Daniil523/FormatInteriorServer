from django.urls import path
from tusk_manager.views import TasksView, ObjectsView, ObjectView, UserObjectsView, UserTasksView, TaskView, \
    CategoriesView, ServiceCategoryView, UserView, WorkersView, TaskObjectView, TaskAddView, AddObjectView

urlpatterns = [
    #API работы с объектами
    path('api/objects/', ObjectsView.as_view({'get': 'list', 'post': 'create'})),
    path('api/addObject/', AddObjectView.as_view({'post': 'create'})),
    path('api/user_objects/', UserObjectsView.as_view({'get': 'list'})),
    path('api/objects/<int:pk>/', ObjectView.as_view({'get': 'list', 'put': 'update', 'delete': 'destroy'})),
    #API работы с задачами
    path('api/tasks/', TasksView.as_view({'get': 'list', 'post': 'create'})),
    path('api/task/add/', TaskAddView.as_view({'post': 'create'})),
    path('api/user_tasks/', UserTasksView.as_view({'get': 'list'})),
    path('api/tasks/<int:pk>/', TaskView.as_view({'get': 'list', 'put': 'update', 'delete': 'destroy'})),
    path('api/changeTasks/<int:pk>/', TaskAddView.as_view({'put': 'update'})),
    path('api/tasks_object/<int:obj>/', TaskObjectView.as_view({'get': 'list'})),
    #API работы с категориями, услугами и пользователями
    path('api/categories/', CategoriesView.as_view({'get': 'list'})),
    path('api/service_categories/<int:pk>/', ServiceCategoryView.as_view({'get': 'list'})),
    path('api/workers/', WorkersView.as_view({'get': 'list', 'post': 'create'})),
    path('api/users/<int:pk>/', UserView.as_view({'get': 'list', 'put': 'update', 'delete': 'destroy'})),
]

