from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext

from sccop.models import *

# Create your views here.

def master(request):
	return render_to_response('master.html', {}, RequestContext(request))

def dashboard(request, username):
	if username:
		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			return render_to_response('dashboard.html', {'msg': 'there is no record with this username'}, RequestContext(request))			
		return render_to_response('dashboard.html', {'user': user}, RequestContext(request))
	return render_to_response('dashboard.html', {'msg': 'please enter your username'}, RequestContext(request))