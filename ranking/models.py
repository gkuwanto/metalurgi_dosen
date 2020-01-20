from django.db import models

# Create your models here.
class Teacher(models.Model):
    capacity = models.IntegerField(default=9)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Student(models.Model):
    nim = models.IntegerField(unique=True)
    ipk = models.FloatField()
    pilihan = models.ForeignKey('Teacher',models.CASCADE)
    def __str__(self):
        return str(self.nim)