"""
rest.py
"""

from django.db import models
from django.urls import path
from rest_framework import serializers, generics


class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class TaskList(generics.ListCreateAPIView):
    # queryset = Task.objects.all()
    serializer_class = TaskSerializer


urlpatterns = [
    path("tasks/", TaskList.as_view(), name="tasks"),]
