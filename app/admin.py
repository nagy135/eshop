import os
from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory


from .models import (
    User,
    Bucket,
    Order,
    Item,
    Image,
    Category
)


class MyAdmin(TreeAdmin):
    form = movenodeform_factory(Category)


site_name = os.environ.get('NAME')
site_name = site_name if site_name is not None else 'example-shop'

admin.site.site_title = site_name
admin.site.site_header = site_name

admin.site.register(User)
admin.site.register(Bucket)
admin.site.register(Order)
admin.site.register(Item)
admin.site.register(Image)
admin.site.register(Category, MyAdmin)
