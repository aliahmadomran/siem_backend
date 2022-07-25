import json
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from network.queryBuilder import ElasticQuery
from network.siem_apis import elasticRequest


@api_view(['GET'])
def get_alerts(request):
    obj = ElasticQuery()
    details = {
    "field": None,
    "field_size": None,
    "date_range": {
        "start": "",
        "end": ""
    },
    "range": [
        {
            "field": "rule.level",
            "gte":'',
            "lte": "12"
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
    # response = requests.request("GET", url, headers=headers, data=payload,verify=False)
    response = elasticRequest(body=payload,api_endpoint=endpoint)
    return JsonResponse({"count":response.json()["count"]}, safe=False, status=status.HTTP_200_OK)