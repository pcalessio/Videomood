from django.shortcuts import render_to_response 
from django.template import RequestContext

def search(request):
    mydata = "a"
    return render_to_response('VideoMoodApp/search.html', mydata, context_instance=RequestContext(request))

def insert(request):
    mydata = "a"
    return render_to_response('VideoMoodApp/insert.html', mydata, context_instance=RequestContext(request))

def result(request):
    mydata = "a"
    return render_to_response('VideoMoodApp/result.html', mydata, context_instance=RequestContext(request))


#def index(request):
#    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
#    return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})
