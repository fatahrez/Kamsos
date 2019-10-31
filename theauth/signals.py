from django.db.models.signals import post_save
from django.dispatch import receiver

from profiles.models import Profile
from theauth.models import User, Pastoralist


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=Pastoralist)
def create_pastoralist_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Pastoralist)
def save_pastoralist_profile(sender, instance, **kwargs):
    instance.profile.save()
