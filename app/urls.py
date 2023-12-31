from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("items", views.items, name="items"),
    path("categories", views.categories, name="categories"),
    path("images", views.images, name="images"),
    path("add_to_bucket", views.add_to_bucket, name="add_to_bucket"),
    path("remove_from_bucket", views.remove_from_bucket, name="remove_from_bucket"),
    path("get_bucket", views.get_bucket, name="get_bucket"),
    path("configuration", views.configuration, name="configuration"),
    path("get_or_create_user", views.get_or_create_user, name="get_or_create_user"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
