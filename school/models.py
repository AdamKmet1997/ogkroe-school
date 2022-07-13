from django.db import models
from embed_video.fields import EmbedVideoField
from django.utils.timezone import now
from sqlalchemy import null


class Video(models.Model):
    title=models.CharField(max_length=100)
    added = models.DateTimeField(default=now, editable=False)
    description=models.CharField(max_length=100)
    url=EmbedVideoField()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-added']

class Results(models.Model):
    track_name = models.CharField(max_length=100)
    tier_number = models.IntegerField()
    date_raced = models.DateField()
    results_image = models.ImageField(upload_to='results_images/', null=False, blank=False)

 