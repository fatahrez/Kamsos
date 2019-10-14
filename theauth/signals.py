from django.db.models.signals import post_save
from django.dispatch import receiver

from profiles.models import Profile
from theauth.models import Pastoralist


@receiver(post_save, sender=Pastoralist)
def create_related_profile(sender, instance, created, *args, **kwargs):
    if instance and created:
        instance.profile = Profile.objects.create(user=instance)