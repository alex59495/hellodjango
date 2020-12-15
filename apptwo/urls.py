from django.urls import path
from django.urls import register_converter

from apptwo import views
from apptwo import converters

register_converter(converters.TwoDigitConverter, 'dd')

urlpatterns = [
    path('djangorocks/', views.djangorocks),
    path('pictures/<str:category>/', views.picture_detail),
    path('pictures/<str:category>/<int:year>', views.picture_detail),
    path('pictures/<str:category>/<int:year>/<int:month>', views.picture_detail),
    path('pictures/<str:category>/<int:year>/<int:month>/<dd:day>', views.picture_detail)
]
