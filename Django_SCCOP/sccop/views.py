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
            values = get_user_values(user)
        except User.DoesNotExist:
            print "except"
            return render_to_response('dashboard.html', {'msg': 'there is no record with this username'}, RequestContext(request))          
        return render_to_response('dashboard.html', {'user': user, 'values': values}, RequestContext(request))
    return render_to_response('dashboard.html', {'msg': 'please enter your username'}, RequestContext(request))


def logs(request, username):
    if username:
        try:
            user = User.objects.get(username=username)
            values = get_user_values(username)
        except User.DoesNotExist:
            return render_to_response('dashboard.html', {'msg': 'there is no record with this username'}, RequestContext(request))          
        return render_to_response('dashboard.html', {'user': user, 'values': values}, RequestContext(request))
    return render_to_response('dashboard.html', {'msg': 'please enter your username'}, RequestContext(request))


def get_user_values(user):
    values = {}
    values['rpm_values'] = user.get_values('rpm')
    values['speed_values'] = user.get_values('speed')
    values['temp_values'] = user.get_values('temp')
    values['temp_fuel'] = user.get_values('fuel')
    values['rpm_max'] = user.get_max('rpm')
    values['rpm_min'] = user.get_min('rpm')
    values['rpm_avg'] = user.get_avg('rpm')
    values['speed_max'] = user.get_max('speed')
    values['speed_min'] = user.get_min('speed')
    values['speed_avg'] = user.get_avg('speed')
    values['temp_max'] = user.get_max('temp')
    values['temp_min'] = user.get_min('temp')
    values['temp_avg'] = user.get_avg('temp')
    return values
