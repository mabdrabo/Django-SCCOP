from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext

from sccop.models import *

from django.utils import simplejson
from django.core import serializers

# Create your views here.

def master(request):
	some_data_to_dump = {
	   'some_var_1': 'foo',
	   'some_var_2': 'bar',
	}
	data = simplejson.dumps(some_data_to_dump)

	# foos = Foo.objects.all()

	# data = serializers.serialize('json', foos)

	return HttpResponse(data, mimetype='application/json')