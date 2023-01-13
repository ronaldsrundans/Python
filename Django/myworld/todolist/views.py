from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Todolist

def index(request):
  mytodolist = Todolist.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mytodolist': mytodolist,
  }
  return HttpResponse(template.render(context, request))
def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))
def addrecord(request):
  x = request.POST['todoitem']
  todolist = Todolist(todoitem=x)
  todolist.save()
  return HttpResponseRedirect(reverse('index'))
