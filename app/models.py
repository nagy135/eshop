from django.db import models
from django.db.models.deletion import CASCADE
from treebeard.mp_tree import MP_Node
from django.db.models.fields import (
    CharField,
    DateTimeField,
    FloatField,
    IntegerField
)
from django.db.models.fields.related import ForeignKey, ManyToManyField


class User(models.Model):
    name: CharField = CharField(max_length=200)
    email: CharField = CharField(max_length=200)
    address: CharField = CharField(max_length=600)

    created_at: DateTimeField = DateTimeField("created at", auto_now_add=True)


class Bucket(models.Model):
    created_at: DateTimeField = DateTimeField("created at", auto_now_add=True)

    user: ForeignKey = ForeignKey(User, on_delete=CASCADE)


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
    name: CharField = CharField(max_length=200)
    status: CharField = CharField(max_length=200)
    address: CharField = CharField(max_length=600)

    bucket: ForeignKey = ForeignKey(Bucket, on_delete=CASCADE)

    created_at: DateTimeField = DateTimeField("created at", auto_now_add=True)


class Category(MP_Node):
    name = models.CharField(max_length=30)

    node_order_by = ['name']

    def __str__(self):
        return 'Category: {}'.format(self.name)


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
    description: CharField = CharField(max_length=200)
    price: FloatField = FloatField()
    remaining: IntegerField = IntegerField()

    categories: ManyToManyField = ManyToManyField(Category)

    created_at: DateTimeField = DateTimeField("created at", auto_now_add=True)


class BucketItem(models.Model):
    created_at: DateTimeField = DateTimeField("created at", auto_now_add=True)

    item: ForeignKey = ForeignKey(Item, on_delete=CASCADE)
    bucket: ForeignKey = ForeignKey(Bucket, on_delete=CASCADE)


class Image(models.Model):
    name: CharField = CharField(max_length=200)
    path: CharField = CharField(max_length=200)

    item: ForeignKey = ForeignKey(Item, on_delete=CASCADE)

    created_at: DateTimeField = DateTimeField("created at", auto_now_add=True)


