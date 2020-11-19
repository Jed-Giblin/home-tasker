from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    account_owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    account_id = models.UUIDField()
    account_name = models.CharField(max_length=50)
    signup_date = models.DateField()