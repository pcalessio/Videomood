from VideoMoodApp.models import Video, Mood, TagRelation
from django.contrib import admin

admin.site.register(TagRelation)
admin.site.register(Mood)
admin.site.register(Video)