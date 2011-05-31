from django.http import HttpResponse

def search(request):
     return HttpResponse("This is search.")

def restaurantDetail(request, restaurant_id):
     return HttpResponse("You're looking at the restaurant detail of restaurant %s." % restaurant_id)

def nomDetail(request, restaurant_id, nom_id):
     return HttpResponse("You're looking at the nom detail of nom %s." % nom_id)
