from django.contrib import admin

from .models import (
    User,
    Bucket,
    Order,
    Item,
    BucketItem,
    Image,
    Category
)

admin.site.register(User)
admin.site.register(Bucket)
admin.site.register(Order)
admin.site.register(Item)
admin.site.register(BucketItem)
admin.site.register(Image)
admin.site.register(Category)
