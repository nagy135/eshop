from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import (
    CharField,
    DateTimeField,
    FloatField,
    IntegerField
)
from django.db.models.fields.related import ForeignKey


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


# // Use DBML to define your database structure
# // Docs: https://dbml.dbdiagram.io/docs
#
#
# Table users {
#   id integer [primary key]
#   name varchar
#   email varchar
#   address varchar
# }
#
# Table orders {
#   id integer [primary key]
#   bucket_id integer
#   status varchar
# }
#
# Table images {
#   id integer [primary key]
#   item_id integer
#
#   name varchar
#   path varchar
#   created_at timestamp
# }
#
# Table items {
#   id integer [primary key]
#   name varchar
#   description varchar
#   price float
#   status varchar
#   remaining integer
#   created_at timestamp
# }
#
# Table bucket_items {
#   id integer [primary key]
#   item_id integer
#   bucket_id integer
#   amount integer
#   created_at timestamp
# }
#
# Table buckets {
#   id integer [primary key]
#   user_id integer
# }
#
#
# Ref: items.id < images.item_id
# Ref: items.id < bucket_items.item_id
# Ref: buckets.id < bucket_items.bucket_id
# Ref: users.id < buckets.user_id
# Ref: buckets.id < orders.bucket_id
