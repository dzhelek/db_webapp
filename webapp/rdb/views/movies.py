from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

from rdb.models import Movie

def list(request):
    return render(request, 'movies/list.html', {'movies': Movie.objects.all()})

def detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/detail.html', {'movies': movie})

class Create(CreateView):
    model = Movie
    fields = ['name', 'year', 'producer', 'actors']
    template_name = 'movies/create.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('rdb:movies:detail', kwargs={'movie_id': self.object.id})

class Update(UpdateView):
    pass

