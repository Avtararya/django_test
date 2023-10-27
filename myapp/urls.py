from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.list_tasks, name='task-list'),
    path('tasks/<int:pk>/', views.retrieve_task, name='task-detail'),
    path('tasks/create/', views.create_task, name='task-create'),
    path('tasks/update/<int:pk>/', views.update_task, name='task-update'),
    path('tasks/delete/<int:pk>/', views.delete_task, name='task-delete'),
]
