from rest_framework.serializers import IntegerField, Serializer


# Add to bucket

class AddToBucketRequest(Serializer):
    userId = IntegerField(required=True)
    itemId = IntegerField(required=True)


# Get bucket

class GetBucketRequest(Serializer):
    bucketId = IntegerField(required=True)
