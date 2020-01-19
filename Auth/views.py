from django.shortcuts import render
from rest_framework import viewsets
from .models import authenticate
from django.http import JsonResponse
import json
import uuid
from datetime import date
from django.views.decorators.csrf import csrf_exempt
import hashlib
@csrf_exempt
def create(request):
    try:
        token=request.headers.get("Authorization")
    except:
        return JsonResponse({"action":404,"message":"Token required"})
    if validate(token)==False:
        return JsonResponse({"action":401,"message":"Access denied"})
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
    try:
        token=request.headers.get("Authorization")
    except:
        return JsonResponse({"action":404,"message":"Token required"})
    if validate(token)==False:
        return JsonResponse({"action":401,"message":"Access denied"})
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

def validate(token):
    base=str(date.today())
    salt="_3bvihz^gvydh86k0+b34xq&+006^m#l)n@!9=s&t@^*xdyn"
    salt+=base+salt
    result = hashlib.sha256(salt.encode())
    if(result.hexdigest()==token):
        return(True)
    else:
        return(False)