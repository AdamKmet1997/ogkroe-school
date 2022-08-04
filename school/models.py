from django.db import models
from embed_video.fields import EmbedVideoField
from django.utils.timezone import now
from sqlalchemy import null
from .utils import get_file_path


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
    results_image_url = models.URLField(max_length = 200,default=null)

 