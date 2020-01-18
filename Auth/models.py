from django.db import models

class authenticate(models.Model):
    id = models.AutoField(primary_key=False)
    name=models.CharField(max_length=50)
    uid=models.CharField(max_length=39,editable=False)
    image=models.CharField(max_length=250)
    email=models.CharField(max_length=100,primary_key=True)
    mobile=models.CharField(max_length=12)
    dob=models.CharField(max_length=12)
    regno=models.CharField(max_length=10,editable=False)
    created=models.CharField(max_length=10,editable=False)
    last_login=models.CharField(max_length=10)
    department=models.CharField(max_length=5)
    admin=models.BooleanField(default=False)

