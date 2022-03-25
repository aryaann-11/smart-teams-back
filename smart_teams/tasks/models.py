from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    # status = -1 0 1 ==> backlog in-progress completed
    status = models.IntegerField(default=-1)

    def __str__(self):
        return self.title 
    
    def serialize(self):
        return {"title":self.title,"status":self.status,"id":self.id}