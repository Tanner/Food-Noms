from django.db import models
from noms import models as nomModels

class Rating(models.Model):
     nom = models.ForeignKey(nomModels.Nom)

     def __unicode__(self):
          return "Rating %(id)d for %(nom)s" % {'id': self.id, 'nom': self.nom.name}

class Question(models.Model):
     rating = models.ForeignKey(Rating)
     question = models.CharField(max_length=200)
     rate = models.IntegerField()
     hasFreeResponse = models.BooleanField()
     freeResponse = models.CharField(max_length=1000)
