from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  
    
    class Meta:
        model = Task
        fields = ['id', 'caption', 'body', 'user', 'user_id', 'created_at']

    def create(self, validated_data):
        task = Task.objects.create(user_id=self.context['request'].user.id, **validated_data)
        return task







