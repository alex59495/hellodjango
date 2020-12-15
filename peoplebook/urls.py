from django.urls import path
from peoplebook import views

urlpatterns = [
  path('', views.index),
  path('<str:display>', views.index),
  path('<str:name>/details', views.show, name='show-user-path')
]