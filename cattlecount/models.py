from django.db import models
from django.contrib.auth.models import User

# Create your models here.







class Shed(models.Model):
    sname = models.CharField(max_length=255)

class Employee(models.Model):
    shed_id = models.ForeignKey(Shed,related_name="employee", on_delete=models.PROTECT,null=True)
    ename = models.CharField(max_length=255)
    salary = models.IntegerField(null=True)
    jdate = models.CharField(max_length=255)
    jdes = models.CharField(max_length=255)

class Lot(models.Model):
    shed_id = models.ForeignKey(Shed,related_name="lot", on_delete=models.PROTECT,null=True)
    lcap = models.IntegerField(null=True)
    avg_lage = models.CharField(max_length=255)

class Cattle(models.Model):
    lot_id = models.ForeignKey(Lot,related_name="cattle", on_delete=models.PROTECT,null=True)
    ctype = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    date_acq = models.CharField(max_length=255)
    buy_cost = models.IntegerField(null=True)
    sale_price = models.IntegerField(null=True)

class MedRec(models.Model):
    c_id = models.ForeignKey(Cattle,related_name="medrec", on_delete=models.PROTECT,null=True)
    last_ch = models.CharField(max_length=255)
    vac_stat = models.CharField(max_length=255)    