from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from django.utils import simplejson
from collections import OrderedDict
from gewb.models import *

# Create your views here.

def master(request):
    return render_to_response('gewb/master.html', {}, RequestContext(request))


def signup(request):
    if request.POST:
        if 'username' in request.POST and 'wb_id' in request.POST and 'name' in request.POST:
            user, new_object = User.objects.get_or_create(username=request.POST['username'], wb_id=request.POST['wb_id'])
            user.name = request.POST['name']
            user.save()
            request.session['username'] = user.username
            return dashboard(request, dic={'success': "successfuly signed up and logged in as " + user.name})
    return render_to_response('gewb/master.html', {'error': 'enter your username'}, RequestContext(request))


def signin(request):
    if request.POST:
        if 'username' in request.POST and 'wb_id' in request.POST:
            try:
                user = User.objects.get(username=request.POST['username'], wb_id=request.POST['wb_id'])
                request.session['username'] = user.username
                return dashboard(request, dic={'success': "logged in as " + user.name})
            except User.DoesNotExist:
                return render_to_response('gewb/master.html', {'error': 'user not found'}, RequestContext(request))
    return render_to_response('gewb/master.html', {'error': 'enter your username'}, RequestContext(request))


def signout(request):
    if 'username' in request.session:
        del request.session['username']
        return render_to_response('gewb/master.html', {'info': "You've Logged out"}, RequestContext(request))
    return render_to_response('gewb/master.html', {'info': "You've Logged out"}, RequestContext(request))


def dashboard(request, dic={}):
    logged_user = logged_in_user(request)
    if isinstance(logged_user, User):
        try:
            user = User.objects.get(username=request.session['username'])
            trackers = user.get_trackers()
            return render_to_response('gewb/dashboard.html', dict(dic, **{'user':user, 'trackers':trackers}), RequestContext(request))
        except User.DoesNotExist:
            return render_to_response('gewb/master.html', {'error': 'please login'}, RequestContext(request))
    else:
        return logged_user


def add_track(request, username):
    logged_user = logged_in_user(request)
    if isinstance(logged_user, User):
        try:
            user = User.objects.get(username=username)
            t, new_object = Track.objects.get_or_create(user1=logged_user, user2=user)
            if new_object:
                return viewLog(request, username, {'success':'Success!'})
            else:
                return viewLog(request, username, {'info':'You are already tracking each other'})
        except User.DoesNotExist:
            return dashboard(request, {'error':'user not found!'})
    else:
        return logged_user


def delete_track(request, username):
    logged_user = logged_in_user(request)
    if isinstance(logged_user, User):
        try:
            user = User.objects.get(username=username)
            ts = Track.objects.filter(Q(user1=user, user2=logged_user) | Q(user2=user, user1=logged_user))
            for t in ts:
                t.delete()
        except Track.DoesNotExist:
            return dashboard(request, {'error':'You are not tracking each other!'})
        except User.DoesNotExist:
            return dashboard(request, {'error':'user not found!'})
    else:
        return logged_user


def viewLog(request, username, dic={}):
    logged_user = logged_in_user(request)
    if isinstance(logged_user, User):
        try:
            user = User.objects.get(username=username)
            logs = user.get_log()
            isTracking = True if user in logged_user.get_trackers() else False
            return render_to_response('gewb/log.html', dict(dic, **{'user':user, 'logs':logs, 'isTracking':isTracking}), RequestContext(request))
        except User.DoesNotExist:
            return dashboard(request, {'error':'User not found!'})
    else:
        return logged_user


def add_emergency(request):
    namesList = ['lon', 'lat', 'uname', 'cat', 'wbid']
    try:
        if request.GET and all(attr in request.GET for attr in namesList):
            print "API Update, GET request"
            try:
                user = User.objects.get(username=request.GET['uname'])
                Emergency.objects.create(user=user, wb_id=request.GET['wbid'], lon=request.GET['lon'], lat=request.GET['lat'], cat=request.GET['cat'])
                return HttpResponse("DONE")
            except User.DoesNotExist:
                return HttpResponse("username not found")
    except Exception, e:
        return HttpResponse(e)


def logged_in_user(request):
    if 'username' in request.session:
        try:
            return User.objects.get(username=request.session['username'])
        except User.DoesNotExist:
            return signin(request)
    return signin(request)
