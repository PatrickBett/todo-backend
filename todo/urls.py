from django.urls import path
from .views import TodoListCreateAPIView, TodoDestroyAPIView

urlpatterns = [
    path('todos/', TodoListCreateAPIView.as_view(), name='todo-create'),
    path('todos/delete/<int:pk>/', TodoDestroyAPIView.as_view(), name='todo-delete'),
]