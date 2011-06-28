from django.template import RequestContext, loader
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from reviews.models import * 
from noms.models import *
from reviews.add_form import AddForm

def detail(request, review_id):
     try:
          review = Review.objects.get(pk=review_id)
          rateResponses = review.ratingresponse_set.all()
          freeResponses = review.freeresponse_set.all()

          t = loader.get_template("base_detail.html")
          c = RequestContext(request, {"review": review, "rate_responses": rateResponses, "free_responses": freeResponses})
          return HttpResponse(t.render(c))
     except Rating.DoesNotExist:
          raise Http404

@login_required
def add(request, nom_id):
     try:
          nom = Nom.objects.get(pk=nom_id)
          questions = Question.objects.all()

          if not request.user.has_perm("reviews.add_review"):
               t = loader.get_template("base_permission_error.html")
               c = RequestContext(request, {})
               return HttpResponse(t.render(c))

          if request.method == "POST":
               form = AddForm(questions, request.POST)
               if form.is_valid():
                    data = form.cleaned_data

                    review = Review.objects.create(nom=Nom.objects.get(pk=nom_id), user=request.user)
                    for question in questions:
                         id = question.id
                         if question.type == Question.QUESTION_TYPE_RATING:
                              RatingResponse.objects.create(review=review, question=question, rate=data[str(id)])
                         if question.type == Question.QUESTION_TYPE_FREE_RESPONSE:
                              FreeResponse.objects.create(review=review, question=question, freeResponse=data[str(id)])

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
def delete(request, review_id):
     try:
          r = Review.objects.get(pk=review_id)

          if request.user == r.user and request.user.has_perm("reviews.delete_review"):
               r.delete()
          
               t = loader.get_template("base_deleted.html")
               c = RequestContext(request, {})
               return HttpResponse(t.render(c))
          else:
               t = loader.get_template("base_permission_error.html")
               c = RequestContext(request, {})
               return HttpResponse(t.render(c))
     except Review.DoesNotExist:
          raise Http404
