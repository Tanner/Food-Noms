from django.template import RequestContext, loader
from django.http import HttpResponse, Http404
from noms.models import Restaurant, Nom

def index(request):
     t = loader.get_template('base_index.html')
     c = RequestContext(request, {})
     return HttpResponse(t.render(c))

def search(request):
     return HttpResponse("This is search.")

def restaurantDetail(request, restaurant_id):
     try:
          r = Restaurant.objects.get(pk=restaurant_id)
     except Restaurant.DoesNotExist:
          raise Http404
     return HttpResponse("You're looking at the restaurant detail of restaurant %s." % restaurant_id)

def nomDetail(request, restaurant_id, nom_id):
     try:
          n = Nom.objects.get(pk=nom_id)
     except Nom.DoesNotExist:
          # Should we redirect to the restaurant page instead of 404?
          raise Http404
     return HttpResponse("You're looking at the nom detail of nom %s." % nom_id)
