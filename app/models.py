from django.db import models
from django.db.models.deletion import CASCADE
from treebeard.mp_tree import MP_Node
from django.db.models.fields import (
    CharField,
    DateTimeField,
    FloatField,
    IntegerField
)
from django.db.models import ImageField, TextField
from django.db.models.fields.related import ForeignKey, ManyToManyField


class Configuration(models.Model):
    banner = models.FileField(upload_to='banner/')


class User(models.Model):
    name: CharField = CharField(max_length=200)
    email: CharField = CharField(max_length=200)
    address: CharField = CharField(max_length=600)

    created_at: DateTimeField = DateTimeField("created at", auto_now_add=True)

    def __str__(self):
        return self.name


class Category(MP_Node):
    name = models.CharField(max_length=30)

    node_order_by = ['name']

    def __str__(self) -> str:
        return self.name


class Item(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'ACTIVE', 'Active'
        DISABLED = 'DISABLED', 'Disabled'
        SOLD_OUT = 'SOLD_OUT', 'Sold Out'

    status: CharField = CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE,
    )
    name: CharField = CharField(max_length=200)
    description: TextField = TextField(max_length=20000)
    price: FloatField = FloatField()
    remaining: IntegerField = IntegerField()

    categories: ManyToManyField = ManyToManyField(Category)

    created_at: DateTimeField = DateTimeField("created at", auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Bucket(models.Model):
    created_at: DateTimeField = DateTimeField("created at", auto_now_add=True)

    user: ForeignKey = ForeignKey(User, on_delete=CASCADE)
    items: ManyToManyField = ManyToManyField(Item)


class Order(models.Model):
    class Status(models.TextChoices):
        CREATED = 'CREATED', 'Created'
        PENDING = 'PENDING', 'Pending'
        IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
        SHIPPED = 'SHIPPED', 'Shipped'
        DELIVERED = 'DELIVERED', 'Delivered'
        CANCELED = 'CANCELED', 'Canceled'

    status: CharField = CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.CREATED,
    )
    address: CharField = CharField(max_length=600, default='')

    bucket: ForeignKey = ForeignKey(Bucket, on_delete=CASCADE)

    created_at: DateTimeField = DateTimeField("created at", auto_now_add=True)


class Image(models.Model):
    name: CharField = CharField(max_length=200)
    image: ImageField = ImageField(upload_to='images')

    item: ForeignKey = ForeignKey(Item, on_delete=CASCADE)

    created_at: DateTimeField = DateTimeField("created at", auto_now_add=True)

    def __str__(self) -> str:
        return self.name
