from django.urls import path,include
from .views import get_tasks,update_tasks
urlpatterns = [
    path('',get_tasks,name='get_tasks_view'),
    path('update/',update_tasks,name='update_tasks_view'),
]