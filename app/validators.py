from rest_framework.serializers import IntegerField, Serializer, CharField


# Add to bucket

class AddToBucketRequest(Serializer):
    userId = IntegerField(required=True)
    itemId = IntegerField(required=True)


# Get bucket

class GetBucketRequest(Serializer):
    userId = IntegerField(required=True)


# Create user

class GetOrCreateUserRequest(Serializer):
    email = CharField(required=True)

# Remove from bucket

class RemoveFromBucketRequest(AddToBucketRequest):
    pass
