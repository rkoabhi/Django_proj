from django.shortcuts import render, redirect
from .models import Video
from .forms import VideoForm
# Create your views here.

def index(request):
    videos = Video.objects.order_by('-date_added') # reverse the order by using - sign
    context = {'videos': videos} #its like a key value pair
    return render(request, 'videorequest/index.html', context) # context will contain all videos as mentioned in above line


def vrform(request):
    if request.method == 'POST':  #to check to if request is coming from the form
        form = VideoForm(request.POST)  #if yes we need to process the request

        if form.is_valid(): #returns a boolean
            new_req = Video(videotitle=request.POST['videoname'], videodesc=request.POST['videodesc']) #the names on RHS are from forms.py
            new_req.save()
            return redirect('index')
    else:
        form = VideoForm()

    context = {'form': form}




    return render(request, 'videorequest/vrform.html', context)
