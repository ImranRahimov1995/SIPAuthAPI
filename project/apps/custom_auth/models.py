from django.db import models
from django.utils import timezone

from rest_framework.authtoken.models import Token


class ExpiringToken(Token):
    expiration_date = models.DateTimeField()

    def has_expired(self) -> bool:
        return timezone.now() >= self.expiration_date

    def update_lifetime(self) -> None:
        self.expiration_date = timezone.now() + timezone.timedelta(
            seconds=600
        )
        self.save()

    def save(self, *args, **kwargs):
        if not self.pk:
            # Set the expiration date to 10 minutes from now
            self.expiration_date = timezone.now() + timezone.timedelta(
                seconds=600
            )
        return super(ExpiringToken, self).save(*args, **kwargs)
