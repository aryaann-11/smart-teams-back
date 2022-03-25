from django.urls import path,include
from .views import get_tasks
urlpatterns = [
    path('/',get_tasks,name='get_tasks_view'),
]