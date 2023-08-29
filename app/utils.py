import os
import json
from pprint import pprint
from django.db.models import Model
from django.core.serializers import serialize


def serialize_model(model: Model) -> str:
    data = serialize('json', [model,])
    struct = json.loads(data)
    data = json.dumps(struct[0])
    return data


def collect_related(li: list, key: str, target: str) -> list:
    res = {}

    for item in li:
        key_i = item[key]
        if key_i in res:
            res[key_i][target].append(item[target])
        else:
            res[key_i] = item
            res[key_i][target] = [item[target]] if item[target] is not None else []

    return [res[k] for k in res]

def attach_currency_to_records(records: list, key: str):
    currency = os.environ.get('CURRENCY', '€')
    for record in records:
        record[key] = str(record[key]) + ' ' + currency
