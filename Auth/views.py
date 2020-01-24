from django.shortcuts import render
from rest_framework import viewsets
from .models import authenticate,adminTransaction
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
    dob="**********"
    created=str(date.today())
    last_login=str(date.today())
    uid=str(uuid.uuid4())
    try:
        k=authenticate.objects.get(email=email)
        if(k.regno=="**********"):
            return JsonResponse({"action":1,"message":"Sign up","uid":k.uid})
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
@csrf_exempt
def admin_tasks(request):
    if request.method=='GET':
        try:
            token=request.headers.get("Authorization")
        except:
            return JsonResponse({"action":404,"message":"Token required"})
        if validate(token)==False:
            return JsonResponse({"action":401,"message":"Access denied"})
        data = request.body.decode('utf-8')
        data = json.loads(data)
        uid=data["uid"]
        try:
            k=authenticate.objects.get(uid=uid)
            return JsonResponse({"action":201,"isAdmin":k.admin})
        except:
             return JsonResponse({"action":401,"message":"User dosen't exists"})
    elif request.method=='POST':
        try:
            token=request.headers.get("Authorization")
        except:
            return JsonResponse({"action":404,"message":"Token required"})
        if validate(token)==False:
            return JsonResponse({"action":401,"message":"Access denied"})
        data = request.body.decode('utf-8')
        data = json.loads(data)
        from_uid=data["from"]
        to_uid=data["to"]
        try:
            k=authenticate.objects.get(uid=from_uid)
            if k.admin==True:
                try:
                    l=authenticate.objects.get(uid=to_uid)
                    if l.admin == False:
                        authenticate.objects.filter(uid=to_uid).update(admin=True)
                        new=adminTransaction(to=to_uid,by=from_uid,date=str(date.today()))
                        new.save()
                        return JsonResponse({"action":1,"message":"success"})
                    else:
                        return JsonResponse({"action":400,"message":"To user already a admin"})
                except:
                    return JsonResponse({"action":401,"message":"To user dosen't exists"})
            else:
                return JsonResponse({"action":400,"message":"From user is not admin"})
        except:
             return JsonResponse({"action":401,"message":"From user dosen't exists"})
def validate(token):
    base=str(date.today())
    salt="_3bvihz^gvydh86k0+b34xq&+006^m#l)n@!9=s&t@^*xdyn"
    salt+=base+salt
    result = hashlib.sha256(salt.encode())
    if(result.hexdigest()==token):
        return(True)
    else:
        return(False)