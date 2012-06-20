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
    num_tag = models.IntegerField(default=0)

    def __unicode__(self):  
        return str(self.video) + ', ' + str(self.mood) + ', ' + str(self.num_tag)    
        
    class Meta:
        unique_together = ('video', 'mood')
        
class Utils(): 

    @staticmethod
    def insertNewVideo(video_id, mood_name, category=''):
        video, created = Video.objects.get_or_create(video_id=video_id)
        mood, created2 = Mood.objects.get_or_create(mood_name=mood_name)
        Utils._insertNewVideo(video, mood)
        video.category=category
        video.save()
    
    @staticmethod
    def _insertNewVideo(video_input, mood_input):
        tr, created = TagRelation.objects.get_or_create(video_id=video_input, mood=mood_input)
        tr.num_tag = tr.num_tag + 1
        tr.save(); 
    
    @staticmethod
    def getVideosFromMood(mood_name):
        v = Video.objects.filter(mood=mood_name)
        return v    


#    @staticmethod
#    def insertNewVideo2(video_input, mood_input):
#        #check if the relation video-mood exists already
#        #vid = Video.objects.filter(video_id=video_input.video_id, mood=mood_input)
#        vid = TagRelation.objects.filter(video_id=video_input, mood=mood_input)
#        if vid:
#            tr = TagRelation.objects.get(video=video_input, mood=mood_input)
#            tr.num_tag = tr.num_tag + 1
#            tr.save()
#        else:
#            #insert
#            m1 = TagRelation(video=video_input, mood=mood_input, num_tag=1)
#            m1.save()
    
    
    
    