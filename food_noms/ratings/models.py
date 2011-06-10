from django.db import models
from noms import models as nomModels

class Rating(models.Model):
     nom = models.ForeignKey(nomModels.Nom)

     def __unicode__(self):
          return "Rating %(id)d for %(nom)s" % {'id': self.id, 'nom': self.nom.name}

class Question(models.Model):
     question = models.CharField(max_length=200)
     hasRate = models.BooleanField()
     hasFreeResponse = models.BooleanField()

     def __unicode__(self):
          return self.question;

class Response(models.Model):
     rating = models.ForeignKey(Rating)
     question = models.ForeignKey(Question, related_name="+")

     rate = models.IntegerField()
     freeResponse = models.CharField(max_length=1000)

     def __unicode__(self):
          return "Response %(id)d for %(rating)s" % {'id': self.id, 'rating': self.rating}
