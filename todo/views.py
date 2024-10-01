from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import TodoSerializer, UserSerializer
from .models import Todo


class TodoListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    # This functions ensures that every Todo is assigned to every User who created it
    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(author = user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author = self.request.user)
        else:
            print(serializer.errors)
        
    


#Delete Todo
class TodoDestroyAPIView(generics.DestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(author = user)

    

# Api View for creating a new user
class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer    
    permission_classes = [AllowAny]

