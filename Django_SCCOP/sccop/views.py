from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext

from sccop.models import *

# Create your views here.

def master(request):
	if 'username' in request.GET:
		user = User.objects.get(username=request.GET['username'])
		return render_to_response('master.html', {'user': user}, RequestContext(request))

	return render_to_response('master.html', {'msg': 'enter a correct username'}, RequestContext(request))