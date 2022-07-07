from pydoc import describe
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Video
from django.views.decorators.csrf import csrf_exempt 
from django.utils.timezone import now
from django.contrib.auth import authenticate, login


def index(request):
    videos = Video.objects.filter(added__lte=now())
    context={"video":videos}
    # print(videos)
    return render(request,"school/index.html",context)

def add(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        url = request.POST.get("url")

        Video.objects.create(title=title,description=description,url=url)

        return HttpResponseRedirect(reverse(index))

    return render(request,"school/add_video.html")

def delete(request,id):
    video = Video.objects.get(id=id)
    video.delete()
    return HttpResponseRedirect(reverse(index))