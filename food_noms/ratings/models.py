from django.db import models
from django.contrib.auth import models as authModels
from noms import models as nomModels

class Rating(models.Model):
     nom = models.ForeignKey(nomModels.Nom)
     user = models.ForeignKey(authModels.User, null=True)

     @models.permalink
     def get_absolute_url(self):
          return ('ratings.views.detail', {}, {"rating_id": self.id})

     def __unicode__(self):
          return "Rating %(id)d for %(nom)s" % {'id': self.id, 'nom': self.nom.name}

class Question(models.Model):
     QUESTION_TYPE_RATING = "RATING"
     QUESTION_TYPE_FREE_RESPONSE = "FREE_RESPONSE"

     QUESTION_TYPES = (
          (QUESTION_TYPE_RATING, 'Rating'),
          (QUESTION_TYPE_FREE_RESPONSE, 'Free Response'),
     )

     question = models.CharField(max_length=200)
     type = models.CharField(max_length=200, choices=QUESTION_TYPES)

     def __unicode__(self):
          return self.question;

class Response(models.Model):
     RESPONSE_MAX_RATING = 10;

     rating = models.ForeignKey(Rating)
     question = models.ForeignKey(Question, related_name="+")

     rate = models.IntegerField(blank=True, null=True)
     freeResponse = models.CharField(max_length=1000, blank=True, null=True)

     def __unicode__(self):
          return "Response %(id)d for %(rating)s" % {'id': self.id, 'rating': self.rating}
