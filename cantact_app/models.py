from django.db import models

from django.db import models


class accuntmodel(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    melicode = models.IntegerField(max_length=10 , default=0)
    phonnumber = models.IntegerField(max_length=11 , default=0)
    berthday = models.CharField(max_length=100)
    pasword = models.CharField(max_length=100)
    # imageuser = models.ImageField(upload_to='img/user',blank=True,null=True)
    def __str__(self):
        return f"{self.melicode}"
class savecodphon(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    melicode = models.IntegerField(max_length=10 , default=0)
    phonnumber = models.IntegerField(max_length=11 , default=0)
    berthday = models.CharField(max_length=100)
    code = models.IntegerField(max_length=10)
    # imageuser = models.ImageField(upload_to='img/user',blank=True,null=True)
    def __str__(self):
        return f"{self.melicode}"
