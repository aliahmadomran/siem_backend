
import datetime

from soupsieve import select

class ElasticQuery():
    def __init__(self):
        self.query = {}
        pass
    
    def dateFilter(self,startDate,endDate):
        try:
            start = startDate
            start = datetime.datetime.strptime(start, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%dT%H:%M:%S")
        except:
            pass
        try:
            end = endDate
            end = datetime.datetime.strptime(end, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%dT%H:%M:%S")

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
                        "gte": startDate,
                        "lt": endDate
                    }
                }
            }

    def addTerms(self,terms):
        for term in terms:
            self.query["bool"]['must'].append({"term": {str(term['field'])+".keyword": term['value']}})


    def Query(self,requestJson):
        self.requestJson = requestJson
        self.dateFilter(self.requestJson['date_range']['start'],self.requestJson['date_range']['end'])
        self.addTerms(self.requestJson['conditions'])
        #


