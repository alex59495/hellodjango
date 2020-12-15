from django.shortcuts import render
from peoplebook.peoples import people

# Create your views here.
def index(request, display = ''):
  context  = {
    'users': people,
    'display': display
  }

  return render(request, 'peoplebook/index.html', context)

def show(request, name):
  context = {
    'user': people[name]
  }
  return render(request, 'peoplebook/show.html', context)

