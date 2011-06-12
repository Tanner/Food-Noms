from django.db import models

class Restaurant(models.Model):
     name = models.CharField(max_length=150)

     def __unicode__(self):
          return self.name

     @models.permalink
     def get_absolute_url(self):
          return ('noms.views.restaurantDetail', {}, {"restaurant_id": self.id})

class Nom(models.Model):
     restaurant = models.ForeignKey(Restaurant)
     name = models.CharField(max_length=150)
     
     def __unicode__(self):
          return self.name

     @models.permalink
     def get_absolute_url(self):
          return ('noms.views.nomDetail', {}, {"restaurant_id": restaurant.id, "nom_id": self.id})
