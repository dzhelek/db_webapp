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


class Form():
    model = Producer
    fields = ['name', 'address', 'networth']
    template_name = 'form.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('rdb:producers:list')


class Create(Form, CreateView):
    template_name = 'producers/create.html'


class Update(Form, UpdateView):
    template_name = 'producers/edit.html'

