from django.shortcuts import render
from rest_framework import viewsets
from .models import authenticate
from django.http import JsonResponse
import json
import uuid
from datetime import date
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def create(request):
    data = request.body.decode('utf-8')
    data = json.loads(data)
    name=data['name']
    img_src=data['image']
    email=data['email']
    mobile="**********"
    regno="**********"
    dob=data['dob']
    created=str(date.today())
    last_login=str(date.today())
    uid=str(uuid.uuid4())
    try:
        k=authenticate.objects.get(email=email)
        authenticate.objects.filter(uid=k.uid).update(last_login=last_login)
        return JsonResponse({"action":0,"message":"Sign in","uid":k.uid})
    except:
        new=authenticate(name=name,uid=uid,image=img_src,email=email,mobile=mobile,regno=regno,created=created,last_login=last_login,admin=False,department="****",dob=dob)
        new.save()
        return JsonResponse({"action":1,"message":"Sign up","uid":uid})
@csrf_exempt
def update(request):
    data = request.body.decode('utf-8')
    data = json.loads(data)
    uid=data["uid"]
    name=data['name']
    mobile=data["mobile"]
    dob=data['dob']
    regno=data['regno']
    department=data["dept"]
    authenticate.objects.filter(uid=uid).update(name=name,mobile=mobile,regno=regno,dob=dob,department=department)
    return JsonResponse({"action":0,"message":"Sign in","uid":uid})
@csrf_exempt
def test(request):
    return JsonResponse({"message":"success"})