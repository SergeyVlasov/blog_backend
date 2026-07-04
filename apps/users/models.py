import secrets

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    token = models.CharField(
        max_length=256,
        unique=True,
        blank=True
    )

    def generate_token(self):
        self.token = secrets.token_hex(128)   # 256 символов
        self.save(update_fields=["token"])