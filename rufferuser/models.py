from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class RufferUser(AbstractUser):
    bio = models.CharField(max_length=150)
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
        blank=True
    )

    def __str__(self):
        return self.username
