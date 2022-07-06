from ..services.get_last_scan import *

def get_last_scan_controller(params):
    response = get_last_scan_service(params['id'])
    return response.json()