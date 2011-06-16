from django.db import models
from django.db.models import signals
from signals import create_profile
from django.contrib.auth.models import User

class UserProfile(models.Model):
     user = models.ForeignKey(User, unique=True)
     url = models.URLField("Website", blank=True)

# When model instance is saved, trigger creation of corresponding profile
signals.post_save.connect(create_profile, sender=User)
