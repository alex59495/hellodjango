"""hellodjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from Pypymusic.admin import admin_site

from appone import views as views1

urlpatterns = [
  path('devices/', include('mydevices.urls')),
#   path('register/', views1.register, name='register'),
#   path('thanks/<str:name>', views1.thanks, name="thanks"),
#   path('hello/', views1.hello),
#   path('songs/', views1.songs_list),
#   path('songs/add/<str:song_name>/<int:duration>', views1.add_song),
  path('create_player/<int:region_id>', views1.create_player, name='create_player'),
  path('admin/', admin_site.urls),
  path('apptwo/', include('apptwo.urls')),
  path('users/', include('peoplebook.urls'))
]