from django.db import models
from django.utils import timezone

# Rename the model to avoid confusion with Django's built-in User model
class User(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=128,blank=False, null=False)
    CATEGORY_CHOICES = (('M', 'Male'),('F', 'Female'))
    gender = models.CharField(max_length=8, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.firstname + " " + self.lastname

    last_login = models.DateTimeField(default=timezone.now)