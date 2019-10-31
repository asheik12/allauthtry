from django.db import models
from django.utils import timezone
# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=55)
    doj = models.DateField(default=timezone.now)
    age = models.PositiveIntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    emp = models.Manager()
    def __str__(self):
        return self.name

    def get_doj(self):
        return self.doj
