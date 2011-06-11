from django.template import RequestContext, loader
from django.http import HttpResponse, Http404
from ratings.models import Rating, Question, Response
from ratings.add_form import AddForm

def add(request, nom_id):
     questions = Question.objects.all()
     form = AddForm(questions)
     
     t = loader.get_template("base_add.html")
     c = RequestContext(request, {"form": form})
     return HttpResponse(t.render(c))

def delete(request, rating_id):
     try:
          r = Rating.objects.get(pk=rating_id)
          r.delete()
          
          t = loader.get_template("base_deleted.html")
          c = RequestContext(request, {})
          return HttpResponse(t.render(c))
     except Rating.DoesNotExist:
          raise Http404
