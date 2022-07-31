from ..services.get_authentication_failure import *

def get_authentication_failure_controller(params,conditions):
    response = get_authentication_failure_service(startDate= params['startDate'],startDate= params['endDate'],conditions=conditions)
    return response.json()