from django.contrib import admin
from rufferuser.models import RufferUser
from image.models import Image
# Register your models here.
admin.site.register(RufferUser)
admin.site.register(Image)
