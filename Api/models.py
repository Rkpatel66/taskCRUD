from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=20, null=False)
    email = models.CharField(max_length=100, null=False)
    

    def __str__(self):
        return self.name