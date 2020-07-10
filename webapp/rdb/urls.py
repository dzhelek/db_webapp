from django.urls import path, include

from rdb.views import actors, index, movies, producers, spouses

app_name = 'rdb'


class Patterns:
    def __init__(self, view):
        self.patterns = [
            path('', view.list, name='list'),
            path('new/', view.create().as_view(), name='create'),
            path('edit/<int:pk>/', view.update().as_view(), name='edit'),
            path(f'delete/<int:element_id>/', view.delete, name='delete'),
        ]


movies_patterns = Patterns(movies).patterns
actors_patterns = Patterns(actors).patterns
spouses_patterns = Patterns(spouses).patterns
producers_patterns = Patterns(producers).patterns

movies_patterns.append(path('actors/<int:movie_id>/', movies.actors, name='actors'))

urlpatterns = [
    path('', index, name='index'),
    path('movies/', include((movies_patterns, 'movies'))),
    path('actors/', include((actors_patterns, 'actors'))),
    path('spouses/', include((spouses_patterns, 'spouses'))),
    path('producers/', include((producers_patterns, 'producers'))),
]
