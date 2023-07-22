from django.db import models


class reservemodel(models.Model):
    jobreserv = models.CharField(max_length=150,default='0')
    detalereserv = models.CharField(max_length=150,default='0')
    personreserv = models.CharField(max_length=150,default='0')
    timereserv = models.CharField(max_length=150,default='0')
    castreserv = models.CharField(max_length=150,default='0')
    hourreserv = models.CharField(max_length=10,default='0')
    dateshamsireserv = models.CharField(max_length=150,default='0')
    datemiladireserv = models.CharField(max_length=150,default='0')
    yearshamsi = models.CharField(max_length=10,default='0')
    def __str__(self):
        return f"{self.personreserv}"
