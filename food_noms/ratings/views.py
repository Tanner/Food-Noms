from django.template import RequestContext, loader
from django.http import HttpResponse, Http404
from ratings.models import Rating, Question, Response
from noms.models import *
from ratings.add_form import AddForm

def add(request, nom_id):
     questions = Question.objects.all()
     if request.method == "POST":
          form = AddForm(questions, request.POST)
          if form.is_valid():
               data = form.cleaned_data

               rating = Rating.objects.create(nom=Nom.objects.get(pk=nom_id))
               for question in questions:
                    id = question.id
                    if question.hasRate:
                         Response.objects.create(rating=rating, question=question, rate=data[str(id)], freeResponse="")
                    if question.hasFreeResponse:
                         Response.objects.create(rating=rating, question=question, rate=0, freeResponse=data[str(id)])

               t = loader.get_template("base_added.html")
               c = RequestContext(request, {})
               return HttpResponse(t.render(c))
     else:
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
