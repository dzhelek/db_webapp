from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

from rdb.models import Producer

def list(request):
    return render(request, 'producers/list.html', {'producers': Producer.objects.all()})

def delete(request, producer_id):
    if request.method == 'POST':
        Producer.objects.get(id=producer_id).delete()
    return redirect(reverse_lazy('rdb:producers:list'))

class Create(CreateView):
    model = Producer
    fields = ['name', 'address', 'networth']
    template_name = 'producers/create.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('rdb:producers:list')

class Update(UpdateView):
    pass

