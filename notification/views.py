from django.shortcuts import render

from image.models import Image
from rufferuser.models import RufferUser
# Create your views here.


def notification_view(request):
    twip = RufferUser.objects.get(username="twip")
    template = "notifications.html"
    user = request.user
    images = Image.objects.filter(tags=user)
    for image in images:
        image.tags.clear()
        image.save()

    return render(request, template, {"images": images})


def notification_count(request):
    user = request.user
    images = Image.objects.filter(tags=user)
    return render(request, "navbar.html", {"images": images})
