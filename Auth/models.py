from django.db import models

class authenticate(models.Model):
    name=models.CharField(null=True,max_length=50)
    uid=models.CharField(null=True,max_length=39,editable=False)
    image=models.CharField(null=True,max_length=250)
    email=models.CharField(max_length=100,primary_key=True)
    mobile=models.CharField(null=True,max_length=12)
    dob=models.CharField(null=True,max_length=12)
    regno=models.CharField(null=True,max_length=10,editable=False)
    created=models.CharField(null=True,max_length=10,editable=False)
    last_login=models.CharField(null=True,max_length=10)
    department=models.CharField(null=True,max_length=5)
    admin=models.BooleanField(null=True,default=False)

