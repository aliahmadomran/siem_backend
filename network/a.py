import requests
import json

url = "https://192.168.42.198:9200/wazuh-alerts-*/_count"

payload = json.dumps({
  "query": {
    "bool": {
      "filter": [
        {
          "range": {
            "timestamp": {
              "gte": "now-10d/d",
              "lte": "now",
              "format": "yyyy-MM-dd'T'HH:mm:ssZ"
            }
          }
        },
        {
          "range": {
            "rule.level": {
              "gte": "level"
            }
          }
        }
      ]
    }
  }
})
headers = {
  'Authorization': 'Basic d2F6dWg6d2F6dWg=',
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload,verify=False)

print(response.text)