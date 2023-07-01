from django.db import models

class jobsmodel(models.Model):
    job = models.CharField(max_length=150 , default="مدیر")
    employee = models.CharField(max_length=150 , default="مدیریت")
    def __str__(self):
        return f"{self.job}"

class employeemodel(models.Model):
    employee = models.CharField(max_length=150 , default='مدیریت')
    melicod = models.CharField(max_length=10,default='0')
    def __str__(self):
        return f"{self.melicod}"
# class servicmodel(models.Model):
#     servic = models.CharField(max_length=150 , default='')
#     emp = models.CharField(max_length=150 , default='')
#     time = models.CharField(max_length=150 , default='')
#     cast = models.CharField(max_length=150 , default='')
#
#     def __str__(self):
#         return f"{self.servic}"



class workmodel(models.Model):
    work = models.CharField(max_length=150, default='تزریقات')
    cast = models.CharField(max_length=150, default='0')
    def __str__(self):
        return f"{self.work}"