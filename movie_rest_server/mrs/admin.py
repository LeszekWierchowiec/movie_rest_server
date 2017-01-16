from django.contrib import admin
from mrs.models import Person, Movie, Role

# Register your models here.

@admin.register(Person)
class Person(admin.ModelAdmin):
    list_display = ('name', 'ranking', 'birth_date')
    #display = 'name'
    
@admin.register(Movie)
class Movie(admin.ModelAdmin):
    list_display = ('title', 'description', 'director', 'year', 'ranking', 'actor_list')
    
    def actor_list(self, movie):
        return ','.join([str(t) for t in movie.actor.all()])

@admin.register(Role)
class Role(admin.ModelAdmin):
    list_display = ('role', 'movie', 'person')    
