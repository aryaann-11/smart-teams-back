from django.shortcuts import render
from .models import Task
from rest_framework.decorators import api_view
from django.http.response import HttpResponse, HttpResponseBadRequest, JsonResponse
import json
# Create your views here.
@api_view(['GET'])
def get_tasks(request):
    tasks = Task.objects.all()
    tasks = [task.serialize() for task in tasks]
    return JsonResponse({'tasks':tasks},status=200)

@api_view(['POST'])
def update_tasks(request):
    data = json.loads(request.body)
    new_tasks = data['tasks']
    for new_task in new_tasks:
        print(new_task)
        task = Task.objects.get(pk=new_task['id'])
        if not task :
            print("Task with id "+str(new_task['id'])+" not found")
        else:
            task.status = new_task['status']
            task.save()
    return JsonResponse({'message':'tasks updated successfully'}, status=200)
