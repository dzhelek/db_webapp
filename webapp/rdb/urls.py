from django.urls import path, include

from rdb.views import index, movies, producers

app_name = 'rdb'


class Patterns:
    def __init__(self, name, view):
        self.patterns = [
            path('', view.list, name='list'),
            path('new/', view.create().as_view(), name='create'),
            path('edit/<int:pk>/', view.update().as_view(), name='edit'),
            path(f'delete/<int:{name}_id>/', view.delete, name='delete'),
        ]


movies_patterns = Patterns('movie', movies).patterns
producers_patterns = Patterns('producer', producers).patterns

urlpatterns = [
    path('', index, name='index'),
    path('movies/', include((movies_patterns, 'movies'))),
    path('producers/', include((producers_patterns, 'producers'))),
]
