from django.db import models

# Create your models here.

class Monday(models.Model):
    Day=models.CharField(max_length=12)
    Trip=models.CharField(max_length=50)
    Time=models.CharField(max_length=8)
    Purpose=models.CharField(max_length=10)
    Date=models.CharField(max_length=12)
    BookedSeats=models.CharField(max_length=60)
    NumberOfSeats=models.IntegerField()
    EmployeeName=models.CharField(max_length=30)
    EmployeeMobile=models.CharField(max_length=10)
    Code=models.CharField(max_length=8)

    class Meta:
        db_table="Monday"

class Tuesday(models.Model):
    Day=models.CharField(max_length=12)
    Trip=models.CharField(max_length=50)
    Time=models.CharField(max_length=8)
    Purpose=models.CharField(max_length=10)
    Date=models.CharField(max_length=12)
    BookedSeats=models.CharField(max_length=60)
    NumberOfSeats=models.IntegerField()
    EmployeeName=models.CharField(max_length=30)
    EmployeeMobile=models.CharField(max_length=10)
    Code=models.CharField(max_length=8)

    class Meta:
        db_table="Tuesday"

class Wednessday(models.Model):
    Day=models.CharField(max_length=12)
    Trip=models.CharField(max_length=50)
    Time=models.CharField(max_length=8)
    Purpose=models.CharField(max_length=10)
    Date=models.CharField(max_length=12)
    BookedSeats=models.CharField(max_length=60)
    NumberOfSeats=models.IntegerField()
    EmployeeName=models.CharField(max_length=30)
    EmployeeMobile=models.CharField(max_length=10)
    Code=models.CharField(max_length=8)

    class Meta:
        db_table="Wednessday"

class Thursday(models.Model):
    Day=models.CharField(max_length=12)
    Trip=models.CharField(max_length=50)
    Time=models.CharField(max_length=8)
    Purpose=models.CharField(max_length=10)
    Date=models.CharField(max_length=12)
    BookedSeats=models.CharField(max_length=60)
    NumberOfSeats=models.IntegerField()
    EmployeeName=models.CharField(max_length=30)
    EmployeeMobile=models.CharField(max_length=10)
    Code=models.CharField(max_length=8)

    class Meta:
        db_table="Thursday"

class Friday(models.Model):
    Day=models.CharField(max_length=12)
    Trip=models.CharField(max_length=50)
    Time=models.CharField(max_length=8)
    Purpose=models.CharField(max_length=10)
    Date=models.CharField(max_length=12)
    BookedSeats=models.CharField(max_length=60)
    NumberOfSeats=models.IntegerField()
    EmployeeName=models.CharField(max_length=30)
    EmployeeMobile=models.CharField(max_length=10)
    Code=models.CharField(max_length=8)

    class Meta:
        db_table="Friday"
        
class Saturday(models.Model):
    Day=models.CharField(max_length=12)
    Trip=models.CharField(max_length=50)
    Time=models.CharField(max_length=8)
    Purpose=models.CharField(max_length=10)
    Date=models.CharField(max_length=12)
    BookedSeats=models.CharField(max_length=60)
    NumberOfSeats=models.IntegerField()
    EmployeeName=models.CharField(max_length=30)
    EmployeeMobile=models.CharField(max_length=10)
    Code=models.CharField(max_length=8)

    class Meta:
        db_table="Saturday"

class Sunday(models.Model):
    Day=models.CharField(max_length=12)
    Trip=models.CharField(max_length=50)
    Time=models.CharField(max_length=8)
    Purpose=models.CharField(max_length=10)
    Date=models.CharField(max_length=12)
    BookedSeats=models.CharField(max_length=60)
    NumberOfSeats=models.IntegerField()
    EmployeeName=models.CharField(max_length=30)
    EmployeeMobile=models.CharField(max_length=10)
    Code=models.CharField(max_length=8)

    class Meta:
        db_table="Sunday"

