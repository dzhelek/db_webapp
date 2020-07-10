from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

from rdb.models import Actor, Movie, Producer, Spouse


def index(request):
    return render(request, 'index.html', {})


class View:
    def __init__(self, cls, name, fields):
        self.cls = cls
        self.name = name
        self.fields = fields

    def list(self, request):
        return render(request, f'{self.name}/list.html', {f'{self.name}': self.cls.objects.all()})

    def delete(self, request, element_id):
        if request.method == 'POST':
            self.cls.objects.get(id=element_id).delete()
        return redirect(reverse_lazy(f'rdb:{self.name}:list'))

    def create(self):
        class Create(CreateView):
            model = self.cls
            fields = self.fields
            template_name = f'{self.name}/create.html'

            @staticmethod
            def get_success_url(*args, **kwargs):
                return reverse_lazy(f'rdb:{self.name}:list')

        return Create

    def update(self):
        class Update(UpdateView):
            model = self.cls
            fields = self.fields
            template_name = f'{self.name}/edit.html'

            @staticmethod
            def get_success_url(*args, **kwargs):
                return reverse_lazy(f'rdb:{self.name}:list')

        return Update


class MovieView(View):
    def __init__(self, *args):
        super().__init__(*args)

    @staticmethod
    def actors(request, movie_id):
        return render(request, f'actors/list.html',
                {'actors': Actor.objects.filter(movie=movie_id)})


movies = MovieView(Movie, 'movies', ['name', 'year', 'producer', 'actors']) 
actors = View(Actor, 'actors', ['name', 'gender', 'birthdate', 'spouse'])
spouses = View(Spouse, 'spouses', ['name', 'birthdate'])
producers = View(Producer, 'producers', ['name', 'address', 'networth'])

