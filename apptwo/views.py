from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def djangorocks(request):
  return HttpResponse('This is a jazzy response')

def picture_detail(request, category, year = 0, month = 0, day = 0):
  template = loader.get_template('apptwo/index.html')
  
  context = {
    'pictures': [
      {
        'name': 'camion',
        'filename': 'camion_ppsp.png'
      },
      {
        'name': 'ouvrier',
        'filename': 'ouvrier_ppsp.png'
      },
      {
        'name': 'logo',
        'filename': 'logo-ppsp.png'
      }
    ]
  }

  return HttpResponse(template.render(context, request))