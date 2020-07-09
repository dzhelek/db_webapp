from django.urls import path, include

from rdb.views import index, movies

app_name = 'rdb'

movies_patterns = [
    path('', movies.list, name='list'),
    path('<int:movie_id>/', movies.detail, name='detail'),
    path('new/', movies.Create.as_view(), name='create'),
    path('<int:pk>/edit/', movies.Update.as_view(), name='edit'),
]

urlpatterns = [
    path('', index, name='index'),
    path('movies/', include((movies_patterns, 'movies'))),
]
