from rest_framework import serializers


class AddToCartValidator(serializers.Serializer):
    item = serializers.IntegerField(required=True)
