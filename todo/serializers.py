from rest_framework import serializers
from .models import Todo
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','email','first_name','last_name']
        extra_kwargs = {"password":{"write_only":True}}

    def create(self,validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
