import datetime

from siem_apis import siemRequest
class ElasticQuery():
    def __init__(self):
        self.query = {}
        pass
    
    def dateFilter(self,startDate,endDate):
        
        try:
            start = startDate
            if start=='':
                start = datetime.datetime.now() - datetime.timedelta(days=365)
                start.strftime("%Y-%m-%dT%H:%M:%SZ")
            
            else:
                start = start.strftime("%Y-%m-%dT%H:%M:%SZ")
        except:
            pass
        try:
            end = endDate
            if end=='':
                end = datetime.datetime.now()
                end.strftime("%Y-%m-%dT%H:%M:%SZ")
            
            else:
                end = end.strftime("%Y-%m-%dT%H:%M:%SZ")
        except:
            pass
        
        self.query = {
                    "bool": {
                        "must": [
                        ],
                    }
                    }

        if start is not None and start != "":
            self.query['bool']["filter"] = {
                "range": {
                    "date": {
                        "gte": str(start),
                        "lt": str(end),
                        "format":"yyyy-MM-dd'T'HH:mm:ssZ"
                    }
                }
            }

    def addTerms(self,terms):
        for term in terms:
            self.query["bool"]['must'].append({"term": {str(term['field'])+".keyword": term['value']}})

    def queryResponce(self,field,size):
        self.responce = {
            "size":0,
            "query":self.query,
            "aggs":{
                "Count":{
                    "terms": {
                    "field": str(field)+".keyword",
                    "size": size
                }
                }
            }
        }
        pass
    def queryBuilder(self,requestJson={}):
        self.requestJson = requestJson
        self.dateFilter(self.requestJson['date_range']['start'],self.requestJson['date_range']['end'])
        self.addTerms(self.requestJson['conditions'])
        self.queryResponce(field=self.requestJson['field'],size=self.requestJson['size'])
        print('------------------------------------')
        print(self.query)
        print('------------------------------------')
        print(self.responce)
        print('------------------------------------')
        

obj = ElasticQuery()

requestJ = {

        "field":"agents",
        "date_range":{
            "start":"",
            "end":""
                        },
        "conditions":[
            {"field":"d",
             "value":"e"},
            {"field":"f",
             "value":"g"},
            {"field":"h",
             "value":"i"}
                    ],
        "size":100
}

obj.queryBuilder(requestJson=requestJ)
# from siem_backend.dev import *
js = {
    "size": 100,
    "sort": [
        {
            "date": {
                "order": "asc"
            }
        }
    ]
}
end_point = '/wazuh-alerts-*/_search?pretty=true'
data = siemRequest(protocol='https',host='192.168.42.198',port=9200,username='wazuh',password='wazuh',request_type = 'get',api_endpoint =end_point , body=js)
# siemRequest(host=dev_host,username=dev_username,password=dev_password,api_endpoint=endd_point)
data = data.json()
# elasticUrl + "/wazuh-alerts-*/_search?pretty=true",
#                     HttpMethod.POST,
#                     entity,
#                     Object.class
# https://192.168.43.198:9200/