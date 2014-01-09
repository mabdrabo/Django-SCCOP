from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext

from sccop.models import *
from django.utils import simplejson

# Create your views here.

def master(request):
    if request.POST:
        print "POOSSSTTTT REQUESTTTTT!!!!!!!"
        some_data_to_dump = {
           'post_some_var_1': 'foo',
           'post_some_var_2': 'bar',
        }
        data = simplejson.dumps(some_data_to_dump)
        print request
        return HttpResponse(data, content_type='application/json')

    some_data_to_dump = {
       'some_var_1': 'foo',
       'some_var_2': 'bar',
    }
    data = simplejson.dumps(some_data_to_dump)
    print request
    return HttpResponse(data, content_type='application/json')