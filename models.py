from django.db import models

# Create your models here.

class student(models.Model):
	First_Name = models.CharField(max_length=30)
	Last_Name = models.CharField(max_length=30)
	Branch = models.CharField(max_length=10)
	Age = models.IntegerField()
	Email = models.EmailField()


		