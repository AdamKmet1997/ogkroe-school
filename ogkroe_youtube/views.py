from pydoc import describe
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.views.decorators.csrf import csrf_exempt 
from django.utils.timezone import now
from django.contrib.auth import authenticate, login

#this should scrape ogkroe youytube channel and display videos
def index(request):
    return render(request,"ogkroe/index.html")