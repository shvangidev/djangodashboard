# marks/models.py
from django.db import models

class MarkSheet(models.Model):
    hindi = models.IntegerField()
    english = models.IntegerField()
    science = models.IntegerField()
    maths = models.IntegerField()
    total_marks = models.IntegerField()
    

class Student(models.Model):
    name = models.CharField(max_length=255)
    roll_number = models.CharField(max_length=20, unique=True)
    marks = models.OneToOneField(MarkSheet, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
