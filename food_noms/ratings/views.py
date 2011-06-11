from django.template import RequestContext, loader
from django.http import HttpResponse, Http404
from ratings.models import Rating, Question, Response

def add(request, nom_id):
     return HttpResponse("Add a rating")

def delete(request, rating_id):
     return HttpResponse("Delete a rating")
