from django.db import models
from django.contrib.auth.models import User

class ToDoUser(models.Model):
    nick_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')

    def __str__(self):
        return f"{self.nick_name}  {self.last_name}"


# Create your models here.
class Event(models.Model):
    name = models.CharField('Event Name', max_length=80)
    event_date = models.DateTimeField('Event Date')
    description = models.TextField(blank=True)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


