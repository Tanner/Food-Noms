from django.db import models

class Restaurant(models.Model):
     name = models.CharField(max_length=150)

     def __unicode__(self):
          return self.name

     def get_absolute_url(self):
          return "/%i/" % self.id

class Nom(models.Model):
     restaurant = models.ForeignKey(Restaurant)
     name = models.CharField(max_length=150)
     
     def __unicode__(self):
          return self.name

     def get_absolute_url(self):
          return "/%i/%i/" % (self.restaurant.id, self.id)
