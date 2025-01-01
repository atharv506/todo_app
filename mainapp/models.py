from django.db import models

# Create your models here.
# title stauts #pending #done #time #inprogqress    #date-current #priority #date - to be finished  



class TODO(models.Model):
    taskstatus = [
    ("D", "completed"),
    ("P", "pending"),
    ("I", "inprogress"),
    
]
    title = models.CharField(max_length=50)
    status = models.Choices(max_length=2,choices = taskstatus)
    date = models.DateField(auto_now_add=True)
