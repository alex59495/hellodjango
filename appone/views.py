from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# from appone.models import Song
from django.urls import reverse

# def hello(request):
#   return HttpResponse('Hello Django! Appone application')

# def songs_list(request):
#   names = []
#   for s in Song.objects.all():
#     names.append(s.name)

#   body = '<br/>'.join(names)
#   return HttpResponse(body)

# def add_song(request, song_name, duration):
#   song = Song(name=song_name, duration=duration)
#   song.save()
#   return HttpResponse("Song saved at id={}".format(song.id))

# from appone.forms import TestForm

# def register(request):
#   if request.method == "POST":
#     print('In Post Processing')
#     form = TestForm(request.POST)
#     if form.is_valid():
#       name = form.cleaned_data['name']
#       if form.cleaned_data['newsletter']:
#         print('{} added to newletter'.format(form.cleaned_data['email']))
#       print(form)
#       return HttpResponseRedirect(reverse('thanks', args=[name]))
#   else:
#     form = TestForm()
  
#   return render(request, 'register.html', {'form': TestForm})

# def thanks(request, name):
#   return HttpResponse('Thanks {}, your registration is successful!'.format(name))

from appone.forms import PlayerForm
from appone.models import Region

def create_player(request, region_id):
  errors = ''

  try:
    region = Region.objects.get(id=region_id)
  except Region.DoesNotExist:
    region = Region(id=region_id)
    errors = "Region {} does not exist".format(region_id)

  if request.method == "POST":
    form = PlayerForm(request.POST)
    if form.is_valid():
      player = form.save(commit=False)
      player.region = region
      player.save()
      print(player)
      HttpResponse('Thanks {} your {} was created'.format(player.name, player.character_class))
  else:
    form = PlayerForm()

  context = {
    'form': form,
    'region': region,
    'errors': errors,
  }

  return render(request, 'create_player.html', context)
