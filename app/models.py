from django.db import models
from django.db.models.fields import CharField, DateTimeField, FloatField


class Item(models.Model):
    name: CharField = CharField(max_length=200)
    price: FloatField = FloatField()
    added_at: DateTimeField = DateTimeField("added at")
