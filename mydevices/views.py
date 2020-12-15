from django.shortcuts import render
from mydevices.models import Device
from django.http import HttpResponse

# Create your views here.
def index(request):
  devices = Device.objects.all()
  context = {
    'devices': devices
  }
  return render(request, 'index.html', context)

def create(request, os, model):
  device = Device(os=os, model=model)
  device.save()
  return HttpResponse("Device with id {} was created".format(device.id))

def show(request, id):
  try:
    device = Device.objects.get(id=id)
    context = {
      'device': device
    }
  except Device.DoesNotExist:
    return HttpResponse(status=404)

  return render(request, 'show.html', context)

def devices_filter(request, os):
  devices_names = []
  for d in Device.objects.filter(os=os):
    devices_names.append(d.__str__())
  
  body = '<br/>'.join(devices_names)
  return HttpResponse(body)

