from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext

from sccop.models import *
from django.utils import simplejson

# Create your views here.

def updateState(request):
    return addLog(request, namesList = ('rpm', 'speed', 'temp', 'throttle', 'fuel', 'engine'))    


def updateLocation(request):
    return addLog(request, namesList = ('lat', 'lon'))


def addLog(request, namesList):
    try:
        if request.GET and all(attr in request.GET for attr in namesList):
            print "API Update, GET request"
            try:
                user = User.objects.get(username=request.GET['username'])
                for name in namesList:
                    LogValue.objects.create(user=user, title=name, value=request.GET[name])
                return HttpResponse("OK")
            except User.DoesNotExist:
                return HttpResponse("username not found")
    except Exception, e:
        return HttpResponse(e)