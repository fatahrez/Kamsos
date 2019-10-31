from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        'theauth.User', on_delete=models.CASCADE
    )

    image = models.ImageField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
