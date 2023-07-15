from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("items", views.items, name="items"),
    path("categories", views.categories, name="categories"),
    path("images", views.images, name="images"),
    path("add_to_cart", views.add_to_cart, name="add_to_cart"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
