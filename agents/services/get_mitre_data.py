import json
from network.siem_apis import elasticRequest
from network.queryBuilder import ElasticQuery
def get_mitre_data_service(startDate,endDate,conditions = []):
    obj = ElasticQuery()
    details = {
    "date_range": {
        "start": startDate,
        "end":  endDate
    },
    "range": [
    ],
    "conditions": [
    ],
    "query_size": None,
    "query_type": "_count or _search",
    "aggs": {"aggdata": {
            "field": "rule.mitre.tactic",
            "size":5
            }},
    "paging":{"check":False,"page":5,"page_size":10}
    }
    if conditions != [] :
        details["conditions"] = conditions
    
    obj.queryBuilder(requestJson=details)
    payload = json.dumps(dict(obj.responce))
    endpoint = "/wazuh-alerts-*/_search?pretty=true"
    data = elasticRequest(body=payload,api_endpoint=endpoint)
    data = data.json()
    responce = data
    return responce
