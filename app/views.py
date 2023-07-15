from django.http import HttpResponse
from django.core.serializers import serialize

from .models import Category, Item, Image


def index(request):
    return HttpResponse(b"Hello world")


def items(request):
    items = Item.objects.all()
    data = serialize('json', items)
    return HttpResponse(data, content_type='application/json')


def images(request):
    images = Image.objects.filter(item=request.GET.get('item'))
    data = serialize('json', images)
    return HttpResponse(data, content_type='application/json')


def categories(request):
    categories = Category.dump_bulk()
    return HttpResponse(categories, content_type='application/json')
