from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views import generic

from .models import Novel, Genre

def hello_world(request):
    return HttpResponse('Hello World')

def list(request):
    novels = Novel.objects.all()
    return render(request, 'my_novels/list.html', {'novels': novels})

class DetailView(generic.DetailView):
    model = Novel
    template_name = "my_novels/detail.html"

def delete(request, pk):
    novel = Novel.objects.get(pk = pk)
    novel.delete()

    return redirect('my_novels:list')

from .forms import CreateForm
from .controllers.chatgpt import bodyGenerator

def create(request):
    genres = Genre.objects.all()

    if request.method == 'POST':
        form = CreateForm(request.POST, genres = genres)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            form_genres = form.cleaned_data['genres'] #relation N a N

            body = bodyGenerator(description=description, genres=[genre.name for genre in form_genres])

            new_novel = Novel.objects.create(title=title, description=description, body=body)

            new_novel.genre.set(form_genres)
            new_novel.save()

            return redirect('my_novels:list')
        
    form = CreateForm(genres = genres)
    return render(request, 'my_novels/create.html', {'form': form})



