from django.db import models

class jobsmodel(models.Model):
    job = models.CharField(max_length=150 , default="مدیر")
    def __str__(self):
        return f"{self.job}"

