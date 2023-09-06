from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    phone_number = PhoneNumberField(max_length=20, verbose_name='phone_number', unique=True)
