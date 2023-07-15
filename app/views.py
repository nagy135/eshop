from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize

from .models import Item


def index(request):
    return HttpResponse(b"Hello world")


def items(request):
    items = Item.objects.all()
    data = serialize('json', items)
    return HttpResponse(data,kcontent_type='application/json')
