from django.db import models
from datetime import datetime


class Transaction(models.Model):
    date = models.DateField(default=datetime.now())
    time = models.TimeField()
    status = models.CharField(max_length=50)
    count = models.IntegerField()
