from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic

from .models import Novel

def hello_world(request):
    return HttpResponse('Hello World')

def list(request):
    novels = Novel.objects.all()
    return render(request, 'my_novels/list.html', {'novels': novels})

class DetailView(generic.DetailView):
    model = Novel
    template_name = "my_novels/detail.html"

