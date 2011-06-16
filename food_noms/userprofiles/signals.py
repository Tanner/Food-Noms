def create_profile(sender, instance, signal, created, **kwargs):
    """When user is created also create a matching profile."""
 
    from bucket.models import Profile
 
    if created:
        Profile(user = instance).save()
        # Do additional stuff here if needed, e.g.
        # create other required related records
