import decimal, datetime, json


def to_json(res):
    def encoder(obj):
        if isinstance(obj, datetime.date):
            return obj.isoformat()
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
    return json.dumps([dict(r) for r in res], default=encoder)
