from django.http import HttpResponse
from django.template import loader
from .models import Todolist

def index(request):
  mymembers = Todolist.objects.all().values()
  output = ""
  for x in mymembers:
    output += x["todoitem"]
  return HttpResponse(output)
