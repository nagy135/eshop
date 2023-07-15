from django.http import HttpResponse
from django.core.serializers import serialize

from .models import Item


def index(request):
    return HttpResponse(b"Hello world")


def items(request):
    items = Item.objects.all()
    data = serialize('json', items)
    return HttpResponse(data, content_type='application/json')
