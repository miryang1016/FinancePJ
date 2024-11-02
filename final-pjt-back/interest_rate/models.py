from django.db import models

class Rates(models.Model):
    cur_unit = models.TextField(null=True)
    cur_nm = models.TextField(null=True)
    ttb = models.TextField(null=True)
    tts = models.TextField(null=True)