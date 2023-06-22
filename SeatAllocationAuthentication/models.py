from django.db import models

# Create your models here.

class User(models.Model):
    EmployeeName=models.CharField(max_length=100)
    EmployeeEmail=models.EmailField(max_length=100)
    EmployeeMobile=models.CharField(max_length=10)
    Code=models.CharField(max_length=8)
    last_login=models.CharField(max_length=100, default="")

    class Meta:
        db_table="User"