from rest_framework import serializers
from .models import Task

# Serializers converts models into Json
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

