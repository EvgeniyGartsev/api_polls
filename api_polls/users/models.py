import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class UUIDAnonUser(models.Model):
    """Модель хранит id анонимных пользователей"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
