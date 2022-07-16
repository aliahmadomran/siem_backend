from siem_backend.dev import *
from network.siem_apis import siemRequest

def jsonPrettier(data):
    responce_list = []
    for key in data['data'].keys():
        if key == 'total':
            continue
        elif key == 'pending':
            
            responce_list.append({"name":"Agents coverage","value":data['data'][key]})
        else:
            updated_key = str(key).capitalize()
            updated_key = str(updated_key).replace('_', ' ')
            responce_list.append({"name":updated_key,"value":data['data'][key]})

    return responce_list
def get_agent_status_service():
    
    endd_point = 'agents/summary/status?pretty=true'
    data = siemRequest(host=dev_host,username=dev_username,password=dev_password,api_endpoint=endd_point)
    data = data.json()
    data = jsonPrettier(data)
    return data