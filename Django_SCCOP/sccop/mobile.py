from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext

from sccop.models import *

# Create your views here.

def master(request):
	some_data_to_dump = {
       'some_var_1': 'foo',
       'some_var_2': 'bar',
    }
    data = simplejson.dumps(some_data_to_dump)

    return HttpResponse(data, mimetype='application/json')