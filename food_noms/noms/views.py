from django.template import RequestContext, loader
from django.http import HttpResponse, Http404
from noms.models import Restaurant, Nom

def index(request):
     t = loader.get_template("base_index.html")
     c = RequestContext(request, {})
     return HttpResponse(t.render(c))

def search(request):
     t = loader.get_template("base_search.html")
     c = RequestContext(request, {})
     return HttpResponse(t.render(c))

def restaurantDetail(request, restaurant_id):
     try:
          r = Restaurant.objects.get(pk=restaurant_id)
          noms = r.nom_set.all()

          t = loader.get_template("base_restaurant.html")
          c = RequestContext(request, {"restaurant": r, "noms": noms})
          return HttpResponse(t.render(c))
     except Restaurant.DoesNotExist:
          raise Http404

def nomDetail(request, restaurant_id, nom_id):
     try:
          n = Nom.objects.get(pk=nom_id)
          t = loader.get_template("base_nom.html")
          c = RequestContext(request, {"nom": n})
          return HttpResponse(t.render(c))
     except Nom.DoesNotExist:
          # Should we redirect to the restaurant page instead of 404?
          raise Http404
