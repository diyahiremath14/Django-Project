# models.py
from django.db import models

class StudentCIE(models.Model):
    usn = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=10)
    cie_marks = models.IntegerField()
class ExamFee(models.Model):
    name = models.CharField(max_length=100)
    usn = models.CharField(max_length=10)
    semester = models.IntegerField()
    fee_paid = models.BooleanField()
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    hired_date = models.DateField()
    job_title = models.CharField(max_length=50)
    salary = models.IntegerField()
class ExamStudent(models.Model):
    name = models.CharField(max_length=100)
    usn = models.CharField(max_length=10)
    grade = models.CharField(max_length=2)
class FinalYearPlacement(models.Model):
    name = models.CharField(max_length=100)
    usn = models.CharField(max_length=10)
    company = models.CharField(max_length=100)
class Faculty(models.Model):
    fid = models.IntegerField()
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=10)
class StudentGrade(models.Model):
    name = models.CharField(max_length=100)
    usn = models.CharField(max_length=10)
    dept = models.CharField(max_length=20)
    grade = models.CharField(max_length=2)
