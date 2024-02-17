from django.db import models
from django.conf import settings

# Create your models here.

class userprofile(models.Model):
    belongs_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=1024, blank=True)
    # profile_picture = 
    instagram1_text = models.CharField(max_length=1024, blank=True)
    instagram1_link = models.CharField(max_length=1024, blank=True)
    instagram2_text = models.CharField(max_length=1024, blank=True)
    instagram2_link = models.CharField(max_length=1024, blank=True)
    x1_text = models.CharField(max_length=1024, blank=True)
    x1_link = models.CharField(max_length=1024, blank=True)
    x2_text = models.CharField(max_length=1024, blank=True)
    x2_link = models.CharField(max_length=1024, blank=True)
    linkedin1_text = models.CharField(max_length=1024, blank=True)
    linkedin1_link = models.CharField(max_length=1024, blank=True)
    linkedin2_text = models.CharField(max_length=1024, blank=True)
    linkedin2_link = models.CharField(max_length=1024, blank=True)
    discord1_text = models.CharField(max_length=1024, blank=True)
    discord1_link = models.CharField(max_length=1024, blank=True)
    discord2_text = models.CharField(max_length=1024, blank=True)
    discord2_link = models.CharField(max_length=1024, blank=True)
    youtube1_text = models.CharField(max_length=1024, blank=True)
    youtube1_link = models.CharField(max_length=1024, blank=True)
    youtube2_text = models.CharField(max_length=1024, blank=True)
    youtube2_link = models.CharField(max_length=1024, blank=True)

    
    	
    def __str__(self):
        return self.belongs_to.username
