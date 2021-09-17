from django.db import models
from rufferuser.models import RufferUser
# Create your models here.


class Image(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=140)
    image = models.ImageField(upload_to='images/')
    time = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(
        RufferUser,
        related_name="like"
    )
    uploaded_by = models.ForeignKey(
        RufferUser,
        related_name='uploaded_by',
        on_delete=models.CASCADE,
    )
    hashtags = models.CharField(max_length=100)
    tags = models.ManyToManyField(
        RufferUser,
        symmetrical=False,
        related_name="tags",
        blank=True,
    )

    def __str__(self):
        return self.title
