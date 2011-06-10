from django.db import models
from noms import models as nomModels

class Rating(models.Model):
     nom = models.ForeignKey(nomModels.Nom)

     def __unicode__(self):
          return "Rating %(id)d for %(nom)s" % {'id': self.id, 'nom': self.nom.name}

class BaseQuestion(models.Model):
     question = models.CharField(max_length=200)
     hasRate = models.BooleanField()
     hasFreeResponse = models.BooleanField()

     def __unicode__(self):
          return self.question;

class Question(models.Model):
     rating = models.ForeignKey(Rating)
     baseQuestion = models.ForeignKey(BaseQuestion, related_name="+")

     rate = models.IntegerField()
     freeResponse = models.CharField(max_length=1000)
