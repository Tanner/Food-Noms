from django.db import models
from django.contrib.auth import models as authModels
from noms import models as nomModels

class Review(models.Model):
     nom = models.ForeignKey(nomModels.Nom)
     user = models.ForeignKey(authModels.User, null=True)

     @models.permalink
     def get_absolute_url(self):
          return ('reviews.views.detail', {}, {"review_id": self.id})

     def __unicode__(self):
          return "Review %(id)d for %(nom)s" % {'id': self.id, 'nom': self.nom.name}

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
     review = models.ForeignKey(Review)
     question = models.ForeignKey(Question, related_name="+")

     def __unicode__(self):
          return "Response %(id)d for %(review)s" % {'id': self.id, 'review': self.review}

     class Meta:
          abstract = True

class FreeResponse(Response):
     freeResponse = models.CharField(max_length=1000, blank=True, null=True)

     def __unicode__(self):
          return "Free " + Response.__unicode__(self)

class RatingResponse(Response):
     RESPONSE_MAX_RATING = 10;

     rate = models.IntegerField(blank=True, null=True)

     def __unicode__(self):
          return "Rating " + Response.__unicode__(self)
