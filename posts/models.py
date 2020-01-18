from django.db import models

class feeds(models.Model):
    uid=models.CharField(max_length=39,editable=False)
    pid=models.CharField(max_length=39,editable=False)
    description=models.CharField(max_length=4000)
    attachment=models.CharField(max_length=550)
    time=models.CharField(max_length=15)
    date=models.CharField(max_length=10)