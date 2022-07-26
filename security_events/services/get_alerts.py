import json
from network.siem_apis import elasticRequest
from network.queryBuilder import ElasticQuery

def get_alerts_service(startDate,endDate,level):
    obj = ElasticQuery()
    details = {
    "field": None,
    "field_size": None,
    "date_range": {
        "start": startDate,
        "end":  endDate
    },
    "range": [
        {
            "field": "rule.level",
            "gte":str(level),
            "lte": ''
        }
    ],
    "conditions": [
    ],
    "query_size": None,
    "query_type": "_count or _search",
    "aggs": {},
    "paging":{"check":False,"page":5,"page_size":10}
    }
    
    obj.queryBuilder(requestJson=details)
    payload = json.dumps(dict(obj.responce))
    endpoint = "/wazuh-alerts-*/_count"
    data = elasticRequest(body=payload,api_endpoint=endpoint)
    data = data.json()
    responce = {"name":"level 12 or above alerts","value":int(data['count'])}
    return responce
    