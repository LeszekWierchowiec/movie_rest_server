from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.

RANKING = (
    (1, "*"),
    (2, "**"),
    (3, "***"),
    (4, "*****"),
    (5, "******"),
    )

class Person(models.Model):
    name = models.CharField(max_length=32)
    ranking = models.IntegerField(choices=RANKING, null=True)
    birth_date = models.DateField()
    
    def __str__(self):
        return self.name
    
class Movie(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(null=True)
    #director = models.ForeignKey(Person, related_name='movie_director')
    director = models.ForeignKey('Person', related_name='movie_director')
    #dołożyliśmy related_name='movie_director', bo bootstrap krzyczał o blędach
    year = models.IntegerField()
    #actor = models.ManyToManyField(Person, through='Role')
    actor = models.ManyToManyField('Person', through='Role', blank=True, related_name='movie_actors')
    ranking = models.IntegerField(choices=RANKING, null=True)
    
    def __str__(self):
        return self.title
    
class Role(models.Model):
    role = models.CharField(max_length=128, primary_key=True)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name="Movie_movie")
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name="Movie_person")