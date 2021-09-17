import re
from django.shortcuts import (
    render, HttpResponseRedirect, HttpResponse, reverse, redirect)
from image.models import Image
from django.views.generic import View

from rufferuser.models import RufferUser
from image.forms import PostImageForm

# Create your views here.


class PostImage(View):
    def get(self, request):
        form = PostImageForm()
        template = "post.html"
        return render(request, template, {"form": form})

    def post(self, request):
        if request.method == "POST":
            form = PostImageForm(request.POST, request.FILES)
            if form.is_valid():
                data = form.cleaned_data
                image = Image.objects.create(
                    title=data['title'],
                    description=data['description'],
                    image=data['image'],
                    uploaded_by=request.user
                )
                if "@" in image.description:
                    try:
                        pattern = re.compile(r"@\S+")
                        tags = pattern.findall(image.description)
                        for username in tags:
                            username = username.replace("@", "")
                            image.tags.add(
                                RufferUser.objects.get(username=username))
                            image.save()
                    except Exception as e:
                        print(e)
                if "#" in image.description:
                    try:
                        pattern = re.compile(r"#\S+")
                        hashtags = pattern.findall(image.description)
                        for tag in hashtags:
                            image.hashtags.add(tag)
                    except Exception as e:
                        print(e)
                image.save()
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Something went wrong")


def search_view(request):
    template = "search.html"
    if request.method == "POST":
        searched = request.POST['searched']
        if searched:
            images = Image.objects.filter(description__contains=searched)
        else:
            images = Image.objects.all()
        return render(
            request, template, {'searched': searched, 'images': images})
    else:
        return render(request, template, {})


def image_view(request, image_id):
    template = "image.html"
    image = Image.objects.get(id=image_id)
    return render(request, template, {"image": image})


def like_view(request, image_id):
    image = Image.objects.get(id=image_id)
    image.like.add(request.user)
    image.save()
    return redirect(request.META.get('HTTP_REFERER'))


def unlike_view(request, image_id):
    image = Image.objects.get(id=image_id)
    image.like.remove(request.user)
    image.save()
    return redirect(request.META.get('HTTP_REFERER'))
