from django.db import models
# Create your models here.


class Department(models.Model):
    Name = models.CharField(max_length=50)

class Doctor(models.Model):
    Name = models.CharField(max_length=50)
    Surname = models.CharField(max_length=50)
    Staff_number = models.IntegerField()
    ID_number = models.CharField(max_length=50)
    Specialization = models.CharField(max_length=60)
    City = models.CharField(max_length=50)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    Average_Rate = models.FloatField()

class Rooms(models.Model):
    Room_number = models.IntegerField()
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)

class Report(models.Model):
    Date = models.DateField()
    Patient_name = models.CharField(max_length=50)
    Patient_surname = models.CharField(max_length=50)
    Patient_ID_number = models.CharField(max_length=50)
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Conclusion = models.CharField(max_length=50)

class Appointment(models.Model):
    Date = models.DateField()
    Time = models.TimeField()
    Patient_name = models.CharField(max_length=50)
    Patient_surname = models.CharField(max_length=50)
    Patient_ID_number = models.CharField(max_length=50)
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

class Reviews(models.Model):
    Patient_name = models.CharField(max_length=50)
    Patient_surname = models.CharField(max_length=50)
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)