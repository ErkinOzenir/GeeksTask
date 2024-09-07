from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/todolist/', views.list_api_view, name='list'),
    path('api/v1/todolist/<int:id>/', views.details_api_view, name='task_detail')
]