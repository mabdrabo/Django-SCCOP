from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext

from sccop.models import *

# Create your views here.

def master(request):
	user = User.objects.get(username="01005574388")
	return render_to_response('master.html', {'user': user}, RequestContext(request))