from siem_backend.dev import *
from network.siem_apis import siemRequest
def get_all_agents_service(pretty,sort,limit,status,query,select):
    
    endd_point = "/agents?pretty="+pretty+"&sort="+sort+"&limit="+limit+"&status="+status+"&q="+query+"&select="+select
    data = siemRequest(host=dev_host,username=dev_username,password=dev_password,api_endpoint=endd_point)
    return data