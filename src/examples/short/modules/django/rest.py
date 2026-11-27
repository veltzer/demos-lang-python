"""
rest.py
"""

from django.db import models
from django.urls import path
from rest_framework import generics, serializers


class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class TaskList(generics.ListCreateAPIView):
    # queryset = Task.objects.all()  # noqa: ERA001  teaching: kept in the comment for the reader
    serializer_class = TaskSerializer


urlpatterns = [
    path("tasks/", TaskList.as_view(), name="tasks"),]
