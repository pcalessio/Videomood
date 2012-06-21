from django.shortcuts import render_to_response 

def search(request):
    return render_to_response('VideoMoodApp/search.html')

def insert(request):
    return render_to_response('VideoMoodApp/insert.html')

def result(request):
    return render_to_response('VideoMoodApp/result.html')


#def index(request):
#    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
#    return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})
