from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=[('F', 'Female'), ('M', 'Male')])
    birthdate = models.DateField()
    spouse = models.OneToOneField('Spouse', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"actor {self.name}"

class Spouse(models.Model):
    name = models.CharField(max_length=50)
    birthdate = models.DateField()

    def __str__(self):
        return f"spouse {self.name}"

class Movie(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    producer = models.ForeignKey('Producer', on_delete=models.SET_NULL, null=True)
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return f"movie {self.name}"

class Producer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    networth = models.IntegerField()

    def __str__(self):
        return f"producer {self.name}"

