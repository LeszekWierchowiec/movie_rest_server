from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from mrs.serializers import PersonSerializer, MovieSerializer, RoleSerializer
from mrs.models import Person, Movie, Role
from rest_framework import status
from django.http import Http404
from rest_framework import generics


# Create your views here.

class MoviesView(APIView):
    
    def get(self, request, format=None):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True, context={"request": request})
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    #złe pomylony movies z person
    
class PersonDetailsView(APIView):
    
    def get_object(self, pk):
        try:
            return Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            raise Http404
        
    def get (self, request, id, format=None):
        person = self.get.object(id)
        serializer = PersonSerializer(person, many=True, context={"request": request})
        return Response(serializer.data)
    #ten powinien być dobry
    
class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    
class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    
class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
class RoleList(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    
class RoleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer    
        
    