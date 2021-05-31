from rest_framework import serializers
from main.models import Task
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

@api_view(["GET"])
def api_overview_view(request):
    api_urls = {
        "List": "task-list/",
        "Detail": "task-detail/<int:pk>/",
        "Update": "task-update/<int:pk>/",
        "Delete": "task-delete/<int:pk>/",
    }
    return Response(api_urls)

@api_view(["GET"])
def TaskList(request):
    tasks = Task.objects.all()
    # many=True makes all objects in a Model Json and many=False makes only one object
    serializer = TaskSerializer(tasks, many=True)
    
    return Response(serializer.data)

@api_view(["GET"])
def TaskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)

@api_view(["POST"])
def TaskCreate(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(test_no=5)

    return Response(serializer.data)

@api_view(["POST"])
def TaskUpdate(request, pk):
    item = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=item, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(["DELETE"])
def TaskDelete(request, pk):
    item = Task.objects.get(id=pk)
    item.delete()

    return Response("Item was deleted SuccessFully!!")



