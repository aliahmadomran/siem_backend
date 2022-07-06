

from siem_backend.dev import *
from network.siem_apis import siemRequest
def get_agent_status_service():
    
    endd_point = 'agents/summary/status?pretty=true'
    data = siemRequest(host=dev_host,username=dev_username,password=dev_password,api_endpoint=endd_point)
    
    return data