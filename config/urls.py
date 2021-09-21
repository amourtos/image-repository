"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from notification import views as notification_views
from image import views as image_views
from rufferuser import views as user_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home_view, name="home"),
    path('search/', image_views.search_view, name="search"),
    path('register/', user_views.Register.as_view(), name="register"),
    path('notifications/', notification_views.notification_view, name="notification"),
    path('accounts/login/', user_views.LogIn.as_view(), name="login"),
    path('logout/', user_views.logout_view, name="logout"),
    path('postimage/', image_views.PostImage.as_view(), name="post"),
    path('image/<int:image_id>/', image_views.image_view, name="image"),
    path('image/like/<int:image_id>/', image_views.like_view, name="like"),
    path('image/unlike/<int:image_id>/', image_views.unlike_view, name="unlike"),
    path('image/delete/<int:image_id>/', image_views.delete_view, name="delete"),
    path('user/<int:user_id>/', user_views.user_view, name="user"),
    path('user/follow/<int:user_id>/', user_views.follow_view, name="follow"),
    path('user/unfollow/<int:user_id>/',
         user_views.unfollow_view, name="unfollow"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
