from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=100,blank=True)
    completed = models.BooleanField(default=False)
    added_date = models.DateTimeField(auto_now_add=True)
    completed_date= models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.user.username} - {self.title}"