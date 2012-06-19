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


class Utils(): 

    @staticmethod
    def insertNewVideo(video_id, category, mood_name, mood_input):
        video = Video.objects.create(video_id=video_id, category=category)
        mood = Mood.objects.create(mood_name=mood_name, popularity=None )
        Utils.insertNewVideo2(video, mood)
        
    @staticmethod
    def insertNewVideo2(video_input, mood_input):
        #check if the relation video-mood exists already
        numTags=0
        tr = TagRelation.objects.get(video=video_input, mood=mood_input)
        if tr:
            numTags = tr.num_tags
        numTags = numTags+1
        #insert
        m1 = TagRelation(video=video_input, mood=mood_input, num_tag=numTags)
        m1.save()
    