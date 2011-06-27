from django.template import RequestContext, loader
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from ratings.models import * 
from noms.models import *
from ratings.add_form import AddForm

def detail(request, rating_id):
     try:
          rating = Rating.objects.get(pk=rating_id)
          rateResponses = rating.ratingresponse_set.all()
          freeResponses = rating.freeresponse_set.all()

          t = loader.get_template("base_detail.html")
          c = RequestContext(request, {"rating": rating, "rate_responses": rateResponses, "free_responses": freeResponses})
          return HttpResponse(t.render(c))
     except Rating.DoesNotExist:
          raise Http404

@login_required
def add(request, nom_id):
     try:
          nom = Nom.objects.get(pk=nom_id)
          questions = Question.objects.all()

          if not request.user.has_perm("ratings.add_rating"):
               t = loader.get_template("base_permission_error.html")
               c = RequestContext(request, {})
               return HttpResponse(t.render(c))

          if request.method == "POST":
               form = AddForm(questions, request.POST)
               if form.is_valid():
                    data = form.cleaned_data

                    rating = Rating.objects.create(nom=Nom.objects.get(pk=nom_id), user=request.user)
                    for question in questions:
                         id = question.id
                         if question.type == Question.QUESTION_TYPE_RATING:
                              Response.objects.create(rating=rating, question=question, rate=data[str(id)])
                         if question.type == Question.QUESTION_TYPE_FREE_RESPONSE:
                              Response.objects.create(rating=rating, question=question, freeResponse=data[str(id)])

                    t = loader.get_template("base_added.html")
                    c = RequestContext(request, {"nom": nom})
                    return HttpResponse(t.render(c))
          else:
               form = AddForm(questions)
          
          t = loader.get_template("base_add.html")
          c = RequestContext(request, {"form": form, "nom": nom})
          return HttpResponse(t.render(c))
     except Nom.DoesNotExist:
          raise Http404

@login_required
def delete(request, rating_id):
     try:
          r = Rating.objects.get(pk=rating_id)

          if request.user == r.user and request.user.has_perm("ratings.delete_rating"):
               r.delete()
          
               t = loader.get_template("base_deleted.html")
               c = RequestContext(request, {})
               return HttpResponse(t.render(c))
          else:
               t = loader.get_template("base_permission_error.html")
               c = RequestContext(request, {})
               return HttpResponse(t.render(c))
     except Rating.DoesNotExist:
          raise Http404
