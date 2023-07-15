from django.db import models


class reservemodel(models.Model):
    jobreserv = models.CharField(max_length=150,default='m')
    detalereserv = models.CharField(max_length=150,default='m')
    personreserv = models.CharField(max_length=150,default='m')
    timereserv = models.CharField(max_length=150,default='m')
    castreserv = models.CharField(max_length=150,default='m')
    dateshamsireserv = models.CharField(max_length=150,default='m')
    datemiladireserv = models.CharField(max_length=150,default='m')
    yearshamsi = models.CharField(max_length=10,default='m')
    def __str__(self):
        return f"{self.personreserv}"
