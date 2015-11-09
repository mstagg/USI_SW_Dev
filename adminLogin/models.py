from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    pin = models.CharField(max_length = 10)
    is_admin = models.BooleanField(default = False)
    is_teacher = models.BooleanField(default = False)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)

class TokenHistory(models.Model):
    prev_amount = models.IntegerField()
    new_amount = models.IntegerField()
    change_amount = models.IntegerField()
    change_datetime = models.DateTimeField()
    current_amount = models.IntegerField()
