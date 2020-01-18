from django.db import models

class authenticate(models.Model):
    name=models.CharField(max_length=50, primary_key=False)
    uid=models.CharField(max_length=39, primary_key=False)
    image=models.CharField(max_length=250, primary_key=False)
    email=models.EmailField(max_length=80, primary_key=True)
    mobile=models.CharField(max_length=12, primary_key=False)
    dob=models.CharField(max_length=12, primary_key=False)
    regno=models.CharField(max_length=10, primary_key=False)
    created=models.CharField(max_length=10, primary_key=False)
    last_login=models.CharField(max_length=10, primary_key=False)
    department=models.CharField(max_length=5, primary_key=False)
    admin=models.BooleanField(default=False, primary_key=False)

