import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize

from .models import Bucket, Category, Item, Image, User
from .validators import AddToBucketRequest, CreateBucketRequest, GetBucketRequest


# Listing

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


# Logic

@csrf_exempt
def add_to_bucket(request):
    body = json.loads(request.body)

    if not AddToBucketRequest(data=body).is_valid():
        return HttpResponse(status=500)

    bucket_id: int = body["bucket_id"]
    item_id: int = body["item_id"]

    bucket = Bucket.objects.get(pk=bucket_id)
    item = Item.objects.get(pk=item_id)

    bucket.items.add(item)

    return HttpResponse(status=204)


@csrf_exempt
def create_bucket(request):
    body = json.loads(request.body)

    if not CreateBucketRequest(data=body).is_valid():
        return HttpResponse(status=500)

    user_id: int = body["user_id"]

    user = User.objects.get(pk=user_id)

    Bucket.objects.create(user=user)

    return HttpResponse(status=204)


@csrf_exempt
def get_bucket(request):
    body = json.loads(request.body)

    if not GetBucketRequest(data=body).is_valid():
        return HttpResponse(status=500)

    bucket_id: int = body["bucket_id"]

    bucket = Bucket.objects.get(pk=bucket_id)

    data = serialize('json', bucket.items.all())
    return HttpResponse(data, content_type='application/json')
