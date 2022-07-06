from siem_backend.dev import *
from network.siem_apis import siemRequest
def get_last_scan_service(id):
    
    endd_point = "/sca/" + id
    data = siemRequest(host=dev_host,username=dev_username,password=dev_password,api_endpoint=endd_point)
    return data