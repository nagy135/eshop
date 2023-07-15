from rest_framework.serializers import IntegerField, Serializer


# Add to bucket

class AddToBucketRequest(Serializer):
    bucket_id = IntegerField(required=True)
    item_id = IntegerField(required=True)


# Create bucket

class CreateBucketRequest(Serializer):
    user_id = IntegerField(required=True)


# Get bucket

class GetBucketRequest(Serializer):
    bucket_id = IntegerField(required=True)
