from django.db import models

# Create your models here.
# title stauts #pending #done #time #inprogqress    #date-current #priority #date - to be finished  
from django.contrib.auth.models import User


class TODO(models.Model):
    taskstatus = [
    ("D", "Done"),
    ("P", "Pending"),
    ("I", "Inprogress"),
    
]
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=2,choices = taskstatus)
    date = models.DateField(auto_now_add=True)
    priority = models.IntegerField()
