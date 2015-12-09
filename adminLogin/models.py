from django.db import models

# Models

# Mailing list
class List(models.Model):
    name = models.CharField(max_length = 50)
    size = models.IntegerField()


# Site users
class User(models.Model):
    user_name = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    phone = models.BigIntegerField(default = 1234567890)
    pin = models.IntegerField()
    is_admin = models.BooleanField(default = False)
    is_sender = models.BooleanField(default = False)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    active = models.BooleanField(default = 1)
    lists = models.ManyToManyField(List)

class AccountStatus(models.Model):
    security_code = models.CharField(max_length = 8)
    active_code = models.BooleanField(default = True)
    token_amount = models.IntegerField()
    change_date = models.DateTimeField()

class Message(models.Model):
    msg = models.CharField(max_length = 160)
    list = models.CharField(max_length = 50)
    size = models.IntegerField()
    change_date = models.DateTimeField()
