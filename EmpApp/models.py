from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    email=models.EmailField()
class Department(models.Model):
    department_name=models.CharField()
    department_id=models.IntegerField()