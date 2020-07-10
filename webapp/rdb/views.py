from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

from rdb.models import Movie, Producer


def index(request):
    return render(request, 'index.html', {})


class View:
    def __init__(self, cls, name, fields):
        self.cls = cls
        self.name = name
        self.fields = fields

    def list(self, request):
        return render(request, f'{self.name}/list.html', {f'{self.name}': self.cls.objects.all()})

    def delete(self, request, producer_id):
        if request.method == 'POST':
            self.cls.objects.get(id=producer_id).delete()
        return redirect(reverse_lazy(f'rdb:{self.name}:list'))

    def create(self):
        class Create(CreateView):
            model = self.cls
            fields = self.fields
            template_name = f'{self.name}/create.html'

            def get_success_url(self, **kwargs):
                return reverse_lazy(f'rdb:{self.name}:list')

        return Create

    def update(self):
        class Update(UpdateView):
            model = self.cls
            fields = self.fields
            template_name = f'{self.name}/edit.html'

            def get_success_url(self, **kwargs):
                return reverse_lazy(f'rdb:{self.name}:list')

        return Update

movies = View(Movie, 'movies', ['name', 'year', 'producer', 'actors']) 
producers = View(Producer, 'producers', ['name', 'address', 'networth'])

