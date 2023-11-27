from django.db import models
from datetime import datetime


class AvgGraph(models.Model):
    date_start = models.DateField(default=datetime.now())
    date_finish = models.DateField(default=datetime.now())
    is_base = models.BooleanField(default=False)
