from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect, render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from rufferuser.forms import RegisterForm, LoginForm
from rufferuser.models import RufferUser
from image.models import Image
from rufferuser.static.rufferuser.twip import twip_greeting
# Create your views here.


@login_required
def home_view(request):
    template = "index.html"
    following = request.user.following.values("id")
    images = Image.objects.filter(
        uploaded_by=request.user).order_by('time').reverse()
    following_images = Image.objects.filter(uploaded_by__in=following)
    images = images | following_images
    return render(request, template, {'images': images})


@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse("home"))


class LogIn(View):
    def get(self, request):
        template = "login.html"
        form = LoginForm()
        return render(request, template, {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid() and request.method == 'POST':
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data['username'],
                password=data['password'],
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('home')))
            else:
                return HttpResponseRedirect("Something went wrong")
        return render(request, "login.html", {"form": form})


class Register(View):
    def get(self, request):
        form = RegisterForm()
        template = "register.html"
        return render(request, template, {'form': form})

    def post(self, request):
        template = "register.html"
        form = RegisterForm(request.POST or None)
        if request.method == "POST" and form.is_valid():
            data = form.cleaned_data
            user = RufferUser.objects.create_user(
                username=data['username'],
                password=data['password']
            )
            # Hi Twip!
            twip_greeting(user)
            return redirect(reverse('login'))

        return render(request, template, {'form': form})


def user_view(request, user_id):
    user = RufferUser.objects.get(id=user_id)
    images = Image.objects.filter(uploaded_by=user)
    template = "user.html"
    context = {"user": user, "images": images}
    return render(request, template, context)


def follow_view(request, user_id):
    me = request.user
    target = RufferUser.objects.get(id=user_id)
    me.following.add(target)
    me.save()
    return redirect(request.META.get('HTTP_REFERER'))


def unfollow_view(request, user_id):
    me = request.user
    target = RufferUser.objects.get(id=user_id)
    me.following.remove(target)
    me.save()
    return redirect(request.META.get('HTTP_REFERER'))
