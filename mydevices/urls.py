from django.urls import path

from mydevices import views

urlpatterns = [
  path('', views.index),
  path('<int:id>/', views.show),
  path('filter/<str:os>/', views.devices_filter),
  path('add/<str:os>/<str:model>/', views.create)
]
