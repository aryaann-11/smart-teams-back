from django.shortcuts import render
from .models import Task
from rest_framework.decorators import api_view
from django.http.response import HttpResponse, HttpResponseBadRequest, JsonResponse

# Create your views here.
@api_view(['GET'])
def get_tasks(request):
    tasks = Task.objects.all()
    tasks = [task.serialize() for task in tasks]
    return JsonResponse({'tasks':tasks},status=200)