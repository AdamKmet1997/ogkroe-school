from django.db import models
from embed_video.fields import EmbedVideoField
from django.utils.timezone import now


# Create your models here.
class Video(models.Model):
    title=models.CharField(max_length=100)
    added = models.DateTimeField(default=now, editable=False)
    description=models.CharField(max_length=100)
    url=EmbedVideoField()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-added']