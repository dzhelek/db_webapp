from django.urls import path, include

from rdb.views import index, movies, producers

app_name = 'rdb'

movies_patterns = [
    path('', movies.list, name='list'),
    path('new/', movies.Create.as_view(), name='create'),
    path('<int:pk>/edit/', movies.Update.as_view(), name='edit'),
]

producers_patterns = [
    path('', producers.list, name='list'),
    path('new/', producers.Create.as_view(), name='create'),
    path('edit/<int:pk>/', producers.Update.as_view(), name='edit'),
    path('delete/<int:producer_id>/', producers.delete, name='delete'),
]

urlpatterns = [
    path('', index, name='index'),
    path('movies/', include((movies_patterns, 'movies'))),
    path('producers/', include((producers_patterns, 'producers'))),
]
