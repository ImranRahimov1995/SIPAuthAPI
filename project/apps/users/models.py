from django.contrib.auth.models import AbstractUser
from django.db import models

from utils.models.validators import phone_regex


class CustomUser(AbstractUser):
    phone = models.CharField(
        max_length=13,
        validators=[phone_regex],
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username
