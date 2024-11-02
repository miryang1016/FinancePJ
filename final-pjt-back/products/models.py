from django.db import models

# Create your models here.
class DepositProduct(models.Model):
    dcls_month = models.TextField(null=True)
    fin_prdt_cd = models.TextField(unique=True, null=True)
    kor_co_nm = models.TextField(null=True)
    fin_prdt_nm = models.TextField(null=True)
    join_way = models.TextField(null=True)
    click_deposit = models.IntegerField(default=0, null=True)

class DepositOption(models.Model):
    product = models.ForeignKey('DepositProduct', on_delete = models.CASCADE, null=True)
    fin_prdt_cd = models.TextField(null=True)
    intr_rate_type_nm = models.CharField(max_length = 100, null=True)
    intr_rate = models.FloatField(null=True)
    save_trm = models.IntegerField(null=True)

class SavingProduct(models.Model):
    dcls_month = models.TextField(null=True)
    fin_prdt_cd = models.TextField(unique=True, null=True)
    kor_co_nm = models.TextField(null=True)
    fin_prdt_nm = models.TextField(null=True)
    join_way = models.TextField(null=True)
    click_saving = models.IntegerField(default=0, null=True)

class SavingOption(models.Model):
    product = models.ForeignKey('SavingProduct', on_delete = models.CASCADE, null=True)
    fin_prdt_cd = models.TextField(null=True)
    intr_rate_type_nm = models.CharField(max_length = 100, null=True)
    intr_rate = models.FloatField(null=True)
    save_trm = models.IntegerField(null=True)
