from django.db import models

# Create your models here.
class post(models.Model):
    uid=models.CharField(max_length=39,editable=False)
    pid=models.CharField(max_length=39,editable=False)
    description=models.CharField(max_length=4000)
    attachment=models.CharField(max_length=550)
    time=models.CharField(max_length=15)
    date=models.CharField(max_length=10)
    def __str__(self):
        return self.uid
class follow(models.Model):
    to=models.CharField(max_length=39,editable=False)
    by=models.CharField(max_length=39,editable=False)
    date=models.CharField(max_length=10)
    def __str__(self):
        return self.by
class upcoming_feeds(models.Model):
    uid=models.CharField(max_length=39,editable=False)
    seen=models.BigIntegerField()
    def __str__(self):
        return self.uid