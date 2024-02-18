from django.db import models
from django.conf import settings

# Create your models here.

class userprofile(models.Model):
    belongs_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=50)
    description = models.CharField(max_length=1024, blank=True)
    # profile_picture = 

    def __str__(self):
        return self.belongs_to.username

class socialPlatform(models.Model):
    name = models.CharField(max_length=1024)
    link = models.CharField(max_length=1024)
    # icon = 

    def __str__(self):
        return self.name

class userLink(models.Model):
    belongs_to_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    belongs_to_socialplatform = models.ForeignKey(socialPlatform, on_delete=models.CASCADE)
    link = models.CharField(max_length=1024)
    text = models.CharField(max_length=1024)

    def __str__(self):
        return self.belongs_to_user.username
