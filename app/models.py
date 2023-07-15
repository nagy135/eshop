from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    added_at = models.DateTimeField("added at")
