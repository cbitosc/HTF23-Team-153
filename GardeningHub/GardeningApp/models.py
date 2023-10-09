from django.db import models
from django import forms

# Create your models here.


class RegisteredUsers(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    userName = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.firstName} {self.lastName} aka {self.userName}"
