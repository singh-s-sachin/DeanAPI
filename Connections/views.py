from django.shortcuts import render
from rest_framework import viewsets
from .models import post,follow,upcoming_feeds
from Auth.models import authenticate
from Auth.views import getName
from django.http import JsonResponse
import json
import uuid
from datetime import date,datetime
from django.views.decorators.csrf import csrf_exempt
import hashlib
from django.db.models import Max
@csrf_exempt
def addpost(request):
    if request.method == 'POST':
        try:
            token=request.headers.get("Authorization")
        except:
            return JsonResponse({"action":404,"message":"Token required"})
        if validate(token)==False:
            return JsonResponse({"action":401,"message":"Access denied"})
        data = request.body.decode('utf-8')
        data = json.loads(data)
        uid=data["uid"]
        description=data["description"]
        attachment=data["attachment"]
        try:
            k=authenticate.objects.get(uid=uid)
            if k.admin==True:
                pid=uuid.uuid4()
                now=datetime.now()
                new=post(uid=uid,pid=pid,attachment=attachment,description=description,date=str(date.today()),time=str(now. strftime("%H:%M:%S")))
                new.save()
                return JsonResponse({"action":201,"message":"success","pid":pid})
            else:
                return JsonResponse({"action":400,"message":"You are not authorized."})
        except:
            return JsonResponse({"action":404,"message":"User dosent exists."})
    if request.method == 'GET':
        try:
            token=request.headers.get("Authorization")
        except:
            return JsonResponse({"action":404,"message":"Token required"})
        if validate(token)==False:
            return JsonResponse({"action":401,"message":"Access denied"})
        data = request.body.decode('utf-8')
        data = json.loads(data)
        uid=data["uid"]
        return JsonResponse({"action":201,"posts":get_posts(uid)})
@csrf_exempt
def follow_task(request):
    if request.method == 'POST':
        try:
            token=request.headers.get("Authorization")
        except:
            return JsonResponse({"action":404,"message":"Token required"})
        if validate(token)==False:
            return JsonResponse({"action":401,"message":"Access denied"})
        data = request.body.decode('utf-8')
        data = json.loads(data)
        by=data["by"]
        to=data["to"]
        if(isFollow(to,by)):
            return JsonResponse({"action":404,"message":"Already following"})
        else:
            try:
                k=authenticate.objects.get(uid=by)
                k1=authenticate.objects.get(uid=to)
                makeFollow(to,by)
                return JsonResponse({"action":201,"message":"success"})
            except:
                return JsonResponse({"action":400,"message":"User dosent exists"})
    if request.method == 'GET':
        try:
            token=request.headers.get("Authorization")
        except:
            return JsonResponse({"action":404,"message":"Token required"})
        if validate(token)==False:
            return JsonResponse({"action":401,"message":"Access denied"})
        data = request.body.decode('utf-8')
        data = json.loads(data)
        by=data["by"]
        to=data["to"]
        return JsonResponse({"action":201,"isFollowing":isFollow(to,by)})
    if request.method=="DELETE":
        try:
            token=request.headers.get("Authorization")
        except:
            return JsonResponse({"action":404,"message":"Token required"})
        if validate(token)==False:
            return JsonResponse({"action":401,"message":"Access denied"})
        data = request.body.decode('utf-8')
        data = json.loads(data)
        by=data["by"]
        to=data["to"]
        if isFollow(to,by):
            unfollow(to,by)
            return JsonResponse({"action":201,"message":"success"})
        else:
            return JsonResponse({"action":401,"message":"Not following"})
def validate(token):
    print("Edit me")
    return(True)
def makeFollow(to,by):
    new=follow(to=to,by=by,date=str(date.today()))
    new.save()
def isFollow(to,by):
    try:
        flw=follow.objects.get(to=to,by=by)
        return True
    except:
        return False
def unfollow(to,by):
    follow.objects.get(to=to,by=by).delete()
def getFollowings(uid):
    k=follow.objects.filter(by=uid)
    l=[]
    for i in k:
        l.append(i.to)
    return l
def max_feeds():
    k=post.objects.all().aggregate(Max('id'))
    if k['id__max']==None:
        return 0
    return k['id__max']
def get_posts(uid):
    followings=getFollowings(uid)
    try:
        k=upcoming_feeds.objects.get(uid=uid)
        minn=k.seen
        maxx=max_feeds()
        upcoming_feeds.objects.filter(uid=uid).update(seen=maxx)
        feeds=post.objects.filter(id__lt=maxx).filter(id__gte=minn).filter(uid__in=followings)
        l=[]
        for i in feeds:
            feed={}
            feed["name"]=getName(i.uid)
            feed["uid"]=i.uid
            feed["description"]=i.description
            feed["attachment"]=i.attachment
            feed["time"]=i.time
            feed["date"]=i.date
            l.append(feed)
        return l[::-1]
    except:
        return "Null"