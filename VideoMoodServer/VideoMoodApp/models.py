from django.db import models


class Video(models.Model):
    video_id = models.CharField(primary_key=True, max_length=20) 
    category = models.CharField(null=True, blank=True, default='', max_length=20)
    
    def __unicode__(self):
        return self.video_id
    
    
class Mood(models.Model):
    mood_name = models.CharField(primary_key=True, max_length=20)
    popularity = models.FloatField(null=True)
    videos = models.ManyToManyField(Video, through='TagRelation')
    
    def __unicode__(self):
        return self.mood_name
    
    
class TagRelation(models.Model):
    video = models.ForeignKey(Video)
    mood = models.ForeignKey(Mood)
    num_tag = models.IntegerField()

