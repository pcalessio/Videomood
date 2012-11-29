from django.shortcuts import render_to_response 
from django.template import RequestContext
from django.utils import simplejson
from django.http import HttpResponse
from models import Mood
from VideoMoodApp.models import VideoMoodForm, Utils


def search(request):
    #later i will need to pass the data for the tag cloud
    mydata = "a"
    return render_to_response('VideoMoodApp/search.html', mydata, context_instance=RequestContext(request))

#this view is just to try the base template
def base(request):
    #later i will need to pass the data for the tag cloud
    mydata = "a"
    return render_to_response('VideoMoodApp/base.html', mydata, context_instance=RequestContext(request))

def insertOld(request):
    mydata = "a"
    return render_to_response('VideoMoodApp/insert.html', mydata, context_instance=RequestContext(request))

def insert_video(request):
    return HttpResponse(request.POST[u'search_text'])


def result(request):
    query = request.GET.get('query', '')
    if query:
        videos = [x.video_id for x in Utils.getVideosFromMood(query)]
    if not videos:
        return HttpResponse("No results for this query")
    else:
        #json_list = simplejson.dumps(videos)
        return render_to_response('VideoMoodApp/result.html', {"videos": simplejson.dumps(videos)}, context_instance=RequestContext(request))

#for the autocomplete
#TODO: it doesn't work... to be fixed
def lookup(request):
    # Default return list
    results = []
    if request.method == "GET":
        if request.GET.has_key(u'query'):
            value = request.GET[u'query']
            # Ignore queries shorter than length 3
            if len(value) > 2:
                mood_results = Mood.objects.filter(name_mood__startswith=value)
                results = [ x.name_mood for x in mood_results ]
    json = simplejson.dumps(results)
    return HttpResponse(json, mimetype='application/json')

def insert(request):
    if request.method == 'POST': # If the form has been submitted...
        form = VideoMoodForm(request.POST) # A form bound to the POST data 
        if form.is_valid(): # All validation rules pass
            Utils.insertNewVideo(form.cleaned_data['video_id'],form.cleaned_data['mood_name'], form.cleaned_data['category'])
            return HttpResponse('thanks ' + form.cleaned_data['video_id'] +' , ' + form.cleaned_data['category'] +' , ' + form.cleaned_data['mood_name']) 
    else:
        form = VideoMoodForm() # An unbound form
    return render_to_response('VideoMoodApp/insert.html', { 'form': form}, context_instance=RequestContext(request))

#def index(request):
#    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
#    return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})
