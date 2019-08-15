from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        'theauth.User', on_delete=models.CASCADE
    )

    image = models.ImageField(blank=True)

    def __str__(self):
        return self.user.username
