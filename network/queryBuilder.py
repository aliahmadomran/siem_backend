def generateRange(field,gt,lt,format=""):
        rang = {"range":{
            str(field):{}
        }}
        if gt != '' and gt != None :
            rang["range"][str(field)]["gte"]=gt
        if lt != '' and lt != None :
            rang["range"][str(field)]["lte"]=lt
        if format != ''  :
            rang["range"][str(field)]["format"]=format
        return rang

class ElasticQuery():
    def __init__(self):
        self.query = {}
        pass

    def dateFilter(self,startDate,endDate):
        start = startDate
        if start=='':
            start = "now-10d/d"
        
        else:
            start += "+0300"

        end = endDate
        if end=='':
            end = 'now'
        else:
            end += "+0300"
        self.query = {"bool": {}}

        format = "yyyy-MM-dd'T'HH:mm:ssZ"
        if start is not None and start != "":
            self.query['bool']["filter"] = [generateRange("timestamp",str(start),str(end),format)]

    def addTerms(self,terms):
        for term in terms:
            self.query["bool"]['filter'].append({"term": {str(term['field'])+".keyword": term['value']}})

     

    def addRange(self,ranges):
        for rang in ranges:
            self.query["bool"]['filter'].append(generateRange(rang["field"],rang["gte"],rang["lte"]))
    def addAggs(self,aggs = {}):
        
        
        
        if aggs['interval'] != {} :
            self.aggs = {}
            self.aggs = {"parentaggsdata": {"date_histogram": {}}}
            self.aggs["parentaggsdata"]["date_histogram"]["field"]=aggs['interval']["field"]
            try:
                if aggs['interval']["size"] != "":
                    self.aggs["parentaggsdata"]["date_histogram"]["interval"]=aggs['interval']["size"]
            except:
                self.aggs["parentaggsdata"]["date_histogram"]["interval"]="week"
            self.aggs["parentaggsdata"]["date_histogram"]["format"]="yyyy-MM-dd"
            if aggs["aggdata"] !={}:
                self.aggs["parentaggsdata"]["aggs"]={"aggdata":{"terms":{}}}
                self.aggs["parentaggsdata"]["aggs"]["aggdata"]["terms"]["field"]=aggs["aggdata"]["field"]
                try:
                    if aggs["aggdata"]["size"] != "":
                        self.aggs["parentaggsdata"]["aggs"]["aggdata"]["terms"]["size"] = aggs["aggdata"]["size"]
                except:
                    pass

        else:
            self.aggs = {}
            if aggs["aggdata"] !={}:
                self.aggs ={"aggdata":{"terms":{}}}
                self.aggs["aggdata"]["terms"]["field"]=aggs["aggdata"]["field"]
                try:
                    if aggs["aggdata"]["size"] != "":
                        self.aggs["aggdata"]["terms"]["size"] = aggs["aggdata"]["size"]
                except:
                    pass
            
    def queryResponce(self,query_size=100,paging={"check":False}):
        if paging['check']:
            self.pagination(paging)
        else:
            self.normalResponce(query_size)
    
    def normalResponce(self,query_size):
        self.responce={}
        if query_size is not None:
            self.responce["size"]=query_size
        self.responce["query"]=self.query
        self.responce['aggs']=self.aggs
    
    def pagination(self,paging):
        self.responce={}
        self.responce["from"]=paging["page"]*paging["page_size"]
        self.responce["size"]=paging["page_size"]
        self.responce["query"]=self.query
        self.responce['aggs']=self.aggs

    def queryBuilder(self,requestJson={}):
        self.requestJson = requestJson
        self.dateFilter(self.requestJson['date_range']['start'],self.requestJson['date_range']['end'])
        try:
            self.addTerms(self.requestJson['conditions'])
        except:
            pass
        try:
            self.addRange(self.requestJson['range'])
        except:
            pass
        try:
            self.addAggs(aggs =self.requestJson["aggs"])
        except:
            pass
        try:
            self.queryResponce(query_size=self.requestJson['query_size'],paging=self.requestJson["paging"])
        except:
            pass
        

obj = ElasticQuery()

requestJ = {
    "field": "agents",
    "field_size": 100,
    "date_range": {
        "start": "",
        "end": ""
    },
    "range": [
        {
            "field": "level",
            "gte": "15",
            "lte": 10
        }
    ],
    "conditions": [
        {
            "field": "rule.description",
            "value": [
        "Registry Value Entry Added to the System",
        "Registry Value Entry Deleted.",
        "Registry Value Integrity Checksum Changed",
        "Registry Key Integrity Checksum Changed",
        "Registry Key Entry Added to the System"
        ]
        },

        {
            "field": "f",
            "value": "g"
        },
        {
            "field": "h",
            "value": "i"
        }
    ],
    "query_size": 17,
    "query_type": "_count or _search",
    "aggs": {
        "interval": {
            "field": "timestamp",
            "size": "day"
        },
        "aggdata": {
            "field": "rule.description",
        }
    },
    "paging":{"check":False,"page":5,"page_size":10}
}

# obj.queryBuilder(requestJson=requestJ)