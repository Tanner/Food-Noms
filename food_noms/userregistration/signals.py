from registration.signals import user_registered
from django.contrib.auth.models import Permission
from django.dispatch import receiver
import reviews

def user_created(sender, user, request, **kwargs):
     user.user_permissions.add(Permission.objects.get(codename="add_review"))
     user.user_permissions.add(Permission.objects.get(codename="delete_review"))
     user.save()

user_registered.connect(user_created)
