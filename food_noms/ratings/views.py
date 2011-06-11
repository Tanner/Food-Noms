from django.template import RequestContext, loader
from django.http import HttpResponse, Http404
from ratings.models import Rating, Question, Response

def add(request, nom_id):
     return HttpResponse("Add a rating")

def delete(request, rating_id):
     try:
          r = Rating.objects.get(pk=rating_id)
          r.delete()
          
          t = loader.get_template("base_deleted.html")
          c = RequestContext(request, {})
          return HttpResponse(t.render(c))
     except Rating.DoesNotExist:
          raise Http404
