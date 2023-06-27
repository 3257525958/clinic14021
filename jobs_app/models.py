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
