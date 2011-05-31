from django.db import models

class Restaurant(models.Model):
     name = models.CharField(max_length=150)

     def __unicode__(self):
          return self.name
     def __str__(self):
          return __str__()

class Nom(models.Model):
     restaurant = models.ForeignKey(Restaurant)
     name = models.CharField(max_length=150)
     
     def __unicode__(self):
          return self.name + " at " + unicode(self.restaurant)
