from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from django.utils import simplejson
from collections import OrderedDict
from sccop.models import *

# Create your views here.

def master(request):
    return render_to_response('master.html', {}, RequestContext(request))


def signup(request):
    if request.POST:
        if 'username' in request.POST:
            user, new_object = User.objects.get_or_create(username=request.POST['username'])
            request.session['username'] = user.username
            return dashboard(request, dic={'success': "successfuly signed up and logged in as " + user.username})
    return render_to_response('master.html', {'error': 'enter your username'}, RequestContext(request))


def signin(request):
    if request.POST:
        if 'username' in request.POST:
            try:
                user = User.objects.get(username=request.POST['username'])
                request.session['username'] = user.username
                return dashboard(request, dic={'success': "you're logged in as " + user.username})
            except User.DoesNotExist:
                return render_to_response('master.html', {'error': 'user not found'}, RequestContext(request))
    return render_to_response('master.html', {'error': 'enter your username'}, RequestContext(request))


def signout(request):
    if 'username' in request.session:
        del request.session['username']
        return render_to_response('master.html', {'info': "You've Logged out"}, RequestContext(request))
    return render_to_response('master.html', {'info': "You've Logged out"}, RequestContext(request))


def dashboard(request, dic={}):
    if 'username' in request.session:
        try:
            user = User.objects.get(username=request.session['username'])
            objects, extras, locations = get_user_objects(user)
            return render_to_response('dashboard.html', dict(dic, **{'user': user, 'objects': objects, 'extras': extras}), RequestContext(request))
        except User.DoesNotExist:
            return render_to_response('dashboard.html', dict(dic, **{'error': 'user not found'}), RequestContext(request))
    return render_to_response('master.html', {'error': 'please login'}, RequestContext(request))


def log(request):
    if 'username' in request.session:
        try:
            user = User.objects.get(username=request.session['username'])
            objects, extras, locations = get_user_objects(user)
            logs = OrderedDict({})
            for rpm, speed, temp, throttle, fuel, engine in zip(objects['rpm_values'], objects['speed_values'], objects['temp_values'], objects['throttle_values'], objects['fuel_values'], objects['engine_values']):
                logs[rpm.date] = [rpm, speed, temp, throttle, fuel, engine]
            return render_to_response('log.html', {'user': user, 'logs': logs, 'extras': extras, 'locations': locations}, RequestContext(request))
        except User.DoesNotExist:
            return render_to_response('log.html', {'msg': 'there is no record with this username'}, RequestContext(request))          
    return render_to_response('master.html', {'error': 'please login'}, RequestContext(request))


def email_send(request):
    if request.POST:
        if all(attr in request.POST for attr in ('email-from', 'email-subject', 'email-content')):
            from django.core.mail import send_mail
            send_mail(request.POST['email-subject'], request.POST['email-content'], request.POST['email-from'], ['abdrabo.mahmoud@gmail.com'], fail_silently=False)
            return render_to_response('contact.html', {'success': "email sent"}, RequestContext(request))
        else:
            return render_to_response('contact.html', {'error': "email Not sent, please try again later"}, RequestContext(request))


def get_user_objects(user):
    objects = {}
    extras = {}
    locations = {}
    objects['rpm_values'] = user.get('rpm')
    objects['speed_values'] = user.get('speed')
    objects['temp_values'] = user.get('temp')
    objects['throttle_values'] = user.get('throttle')
    objects['fuel_values'] = user.get('fuel')
    objects['engine_values'] = user.get('engine')
    extras['rpm_max'] = user.get_max('rpm')
    extras['rpm_min'] = user.get_min('rpm')
    extras['rpm_avg'] = user.get_avg('rpm')
    extras['speed_max'] = user.get_max('speed')
    extras['speed_min'] = user.get_min('speed')
    extras['speed_avg'] = user.get_avg('speed')
    extras['temp_max'] = user.get_max('temp')
    extras['temp_min'] = user.get_min('temp')
    extras['temp_avg'] = user.get_avg('temp')
    extras['throttle_max'] = user.get_max('throttle')
    extras['throttle_min'] = user.get_min('throttle')
    extras['throttle_avg'] = user.get_avg('throttle')
    extras['fuel_max'] = user.get_max('fuel')
    extras['fuel_min'] = user.get_min('fuel')
    extras['fuel_avg'] = user.get_avg('fuel')
    extras['engine_max'] = user.get_max('engine')
    extras['engine_min'] = user.get_min('engine')
    extras['engine_avg'] = user.get_avg('engine')
    locations['locations'] = user.get_locations()
    return objects, extras, locations


def soundRecord(request):
    return render_to_response('test.html', {}, RequestContext(request))