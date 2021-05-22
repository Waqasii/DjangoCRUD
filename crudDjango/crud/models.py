from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_name=models.TextField(max_length=20)
    emp_email=models.TextField(max_length=20)
    emp_mobile=models.TextField(max_length=20)