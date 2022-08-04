from pydoc import describe
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Results, Video
from django.views.decorators.csrf import csrf_exempt 
from django.utils.timezone import now
from django.contrib.auth import authenticate, login
from .forms import ResultsForm
from django.views.decorators.clickjacking import xframe_options_exempt


def index(request):
    return render(request,"school/index.html")

@xframe_options_exempt
def academy(request):
    videos = Video.objects.filter(added__lte=now())
    context={"video":videos}
    return render(request,"school/academy.html",context)

def add(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        url = request.POST.get("url")

        Video.objects.create(title=title,description=description,url=url)

        return HttpResponseRedirect(reverse(academy))

    return render(request,"school/add_video.html")

def delete(request,id):
    video = Video.objects.get(id=id)
    video.delete()
    return HttpResponseRedirect(reverse(index))

def rules(request):
    return render(request,"school/rules.html")

def results(request):

    if request.method == "POST":
        results_form = ResultsForm(request.POST,request.FILES)

        if results_form.is_valid():
            results_form.save()
            results = Results.objects.all()
            context = {
                "results":results,
                "results_form":results_form
                }
            # return HttpResponseRedirect(reverse(results))
            return render(request,"school/results.html",context)
    else:
        results_form = ResultsForm()

        results = Results.objects.all()
        context = {
            "results":results,
            "results_form":results_form
            }
        print(context)
        return render(request,"school/results.html",context)

def delete_results(request,id):
    results = Results.objects.get(id=id)
    results.delete()
    return HttpResponseRedirect(reverse("results"))

def history(request):
    return render(request,"school/history.html")

def about(request):
    return render(request,"school/about.html")