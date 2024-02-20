from django.urls import path
from . import views

urlpatterns = [
    path('task/', views.TaskList.as_view(), name='task_list'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task_detail'),
    path('performer/', views.PerformerList.as_view(), name='performer_list'),
    path('performer/<int:pk>/', views.PerformerDetail.as_view(), name='performer_detail'),
]
