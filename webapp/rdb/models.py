from django.db import models
from django.utils import timezone


class Actor(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=[('F', 'Female'), ('M', 'Male')])
    birthdate = models.DateField(default=timezone.now)
    spouse = models.OneToOneField('Spouse', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name}"


class Spouse(models.Model):
    name = models.CharField(max_length=50)
    birthdate = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.name}"


class Movie(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    producer = models.ForeignKey('Producer', on_delete=models.SET_NULL, null=True)
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return f"{self.name}"


class Producer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    networth = models.IntegerField()

    def __str__(self):
        return f"{self.name}"

