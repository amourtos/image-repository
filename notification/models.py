from django.db import models
from image.models import Image
# Create your models here.


class Notification(models.Model):
    tags = models.ManyToManyField(
        Image,
        symmetrical=False,
        blank=True
    )
