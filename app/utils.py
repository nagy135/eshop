import json
from django.db.models import Model
from django.core.serializers import serialize


def serialize_model(model: Model) -> str:
    data = serialize('json', [model,])
    struct = json.loads(data)
    data = json.dumps(struct[0])
    return data
