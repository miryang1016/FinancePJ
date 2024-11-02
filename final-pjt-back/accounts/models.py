from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    mainbank = models.CharField(max_length=225, blank=True)
    register = models.CharField(max_length=100, blank=True)
    work = models.CharField(max_length=100, blank=True)
    salary = models.CharField(max_length=100, blank=True)
    money = models.IntegerField(null=True)
    financial_products = models.CharField(max_length=10000, blank=True, null=True)

