from django.db import models

# Themes
class Sitesettings(models.Model):
    banner=models.ImageField(upload_to='media/site/')
    caption=models.TextField()

