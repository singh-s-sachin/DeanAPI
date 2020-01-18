from django.shortcuts import render
from .models import feeds
import uuid
from datetime import date,datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
# Create your views here.
@csrf_exempt
def addpost(request):
    data = request.body.decode('utf-8')
    data = json.loads(data)
    uid=data["uid"]
    pid=uuid.uuid4()
    description=data["desc"]
    attachment=data["attachment"]
    tme=str(datetime.now().time())
    dte=str(date.today())
    try:
        new=feeds(uid=uid,pid=pid,description=description,attachment=attachment,time=tme,date=dte)
        new.save()
        return JsonResponse({"success":1,"message":"success","pid":pid})
    except:
        return JsonResponse({"success":0,"message":"server error"})