from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext

from sccop.models import *
from django.utils import simplejson

# Create your views here.

def add(request):
    try:
        if request.GET:
            print "GEETTTTTT REQUESTTTTT!!!!!!!"
            print "rpm: ", request.GET['rpm']
            print "speed: ", request.GET['speed']
            print "temp: ", request.GET['temp']
            user = User.objects.get(username=request.GET['username'])
            LogValue.objects.create(user=user, title="rpm", value=request.GET['rpm'])
            LogValue.objects.create(user=user, title="speed", value=request.GET['speed'])
            LogValue.objects.create(user=user, title="temp", value=request.GET['temp'])

            return HttpResponse("OK")
    except Exception, e:
        return HttpResponse(e)

    # some_data_to_dump = {
    #    'some_var_1': 'foo',
    #    'some_var_2': 'bar',
    # }
    # data = simplejson.dumps(some_data_to_dump)
    # print request
    # return HttpResponse(data, content_type='application/json')