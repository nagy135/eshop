import json
import os
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize

from eshop.settings import MEDIA_URL

from .utils import collect_related

from .models import Bucket, Category, Configuration, Item, Image, User, Order
from .validators import AddToBucketRequest, GetBucketRequest


# Listing

@csrf_exempt
def items(request):
    category_id = request.GET.get('categoryId')
    page = request.GET.get('page')
    page_size = request.GET.get('pageSize')

    items = Item.objects.all()\
        .prefetch_related('image_set')\
        .values('name', 'price', 'description', 'image__image')

    if category_id is not None:
        items = items.filter(categories__pk=category_id)

    page_size = int(page_size) if page_size is not None else 7
    page = int(page) if page is not None else 0

    items = collect_related(list(items), key='name', target='image__image')
    items *= 3

    # OPTIM: this should be on db level with joins, revisit
    items = items[page*page_size:page*page_size+page_size]

    return HttpResponse(json.dumps(items), content_type='application/json', headers={"Access-Control-Allow-Origin": '*'})


def images(request):
    images = Image.objects.filter(item=request.GET.get('item'))
    data = serialize('json', images)
    return HttpResponse(data, content_type='application/json')


def categories(request):
    categories = Category.dump_bulk()
    return HttpResponse(json.dumps(categories), content_type='application/json')


def configuration(request):
    configuration = Configuration.objects.values('banner', 'id').first()
    if configuration is None:
        return HttpResponse(status=404)
    configuration["banner"] = f"{MEDIA_URL[1:]}{configuration['banner']}"
    configuration["title"] = os.environ.get('NAME', 'website')
    return HttpResponse(json.dumps(configuration), content_type='application/json')


# Logic

@csrf_exempt
def add_to_bucket(request):
    body = json.loads(request.body)

    if not AddToBucketRequest(data=body).is_valid():
        return HttpResponse(status=500)

    item_id: int = body["item_id"]
    user_id: int = body["user_id"]

    item = Item.objects.get(pk=item_id)
    user = User.objects.get(pk=user_id)

    buckets = user.bucket_set\
        .prefetch_related('order_set')\
        .filter(order__status=Order.Status.CREATED)\
        .all()

    if len(buckets):
        bucket = buckets[0]
    else:
        bucket = Bucket.objects.create(user=user)
        Order.objects.create(bucket=bucket)

    bucket.items.add(item)

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
