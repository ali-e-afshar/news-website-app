# accounting/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Super User'),
        (2, 'Admin User'),
        (3, 'Site User'),
        (4, 'External User'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=4)
    mobile_number = models.CharField(max_length=15, unique=True)
