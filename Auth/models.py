from django.db import models

class authenticate(models.Model):
    name=models.CharField(max_length=50)
    uid=models.CharField(max_length=39)
    image=models.CharField(max_length=250)
    email=models.ForeignKey('emails',on_delete=models.CASCADE)
    mobile=models.CharField(max_length=12)
    dob=models.CharField(max_length=12)
    regno=models.CharField(max_length=10)
    created=models.CharField(max_length=10)
    last_login=models.CharField(max_length=10)
    department=models.CharField(max_length=5)
    admin=models.BooleanField(default=False)

class emails(models.Model):
    email=models.CharField(max_length=250)
    uid=models.CharField(max_length=39)